import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [unidade, setUnidade] = useState('');
  const [contadores, setContadores] = useState({});
  const [totalChamados, setTotalChamados] = useState(0);

  // Função para buscar contadores e total de chamados da API
  const fetchData = async () => {
    try {
      const contadoresResponse = await axios.get('http://127.0.0.1:5001/contadores');
      const totalResponse = await axios.get('http://127.0.0.1:5001/total_chamados');

      setContadores(contadoresResponse.data);
      setTotalChamados(totalResponse.data.total);
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
    }
  };

  // Efeito para buscar dados ao montar o componente
  useEffect(() => {
    fetchData();
  }, []);

  // Função para registrar um chamado
  const registrarChamado = async () => {
    if (!unidade) {
      alert("Por favor, selecione uma unidade.");
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:5001/registrar_chamado', { unidade });
      alert(response.data.mensagem);
      fetchData(); // Atualiza os dados após registrar o chamado
    } catch (error) {
      console.error("Erro ao registrar chamado:", error);
    }
  };

  return (
    <div>
      <h1>Registro de Chamados</h1>
      <select value={unidade} onChange={(e) => setUnidade(e.target.value)}>
        <option value="">Selecione uma unidade</option>
        <option value="UPA Alvarenga">UPA Alvarenga</option>
        <option value="UBS Alvarenga">UBS Alvarenga</option>
      </select>
      <button onClick={registrarChamado}>Registrar Chamado</button>

      <h2>Total de Chamados: {totalChamados}</h2>
      <h3>Contadores por Unidade:</h3>
      <ul>
        {Object.entries(contadores).map(([key, value]) => (
          <li key={key}>{key}: {value}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
