//Exibir uma Mensagem:
alert("Olá, mundo!");  // Exibe um alerta com a mensagem "Olá, mundo!"

//Variáveis e Saída:
var nome = "João";
var idade = 30;
console.log("Nome: " + nome);
console.log("Idade: " + idade);

//Condicionais:
var idade = 18;
if (idade >= 18) {
    console.log("Você é maior de idade.");
} else {
    console.log("Você é menor de idade.");
}

//Loops:
for (var i = 1; i <= 5; i++) {
    console.log("Número: " + i);
}

//Funções:
function saudacao(nome) {
    console.log("Olá, " + nome + "!");
}

saudacao("Maria");  // Chama a função e passa "Maria" como argumento

//Arrays (Listas):
var frutas = ["maçã", "banana", "laranja"];
console.log("Primeira fruta: " + frutas[0]);

//Objetos: 
var pessoa = {
    nome: "Carlos",
    idade: 25,
    profissao: "Engenheiro"
};

console.log(pessoa.nome + " tem " + pessoa.idade + " anos.");
