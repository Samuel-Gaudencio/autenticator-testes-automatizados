from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class LoginTests(TestCase):

    def setUp(self):
        """
        Configura o ambiente de teste criando um usuário de teste antes de cada teste.
        """
        # Cria um usuário de teste com nome de usuário "teste", senha "senha123" e email "teste@example.com"
        get_user_model().objects.create_user(username='teste', password='senha123', email='teste@example.com')

    def test_login_success(self):
        """
        Testa o login bem-sucedido com credenciais válidas.
        """
        # Envia uma requisição POST para a view de login com as credenciais corretas
        response = self.client.post(reverse('login'), {'username': 'teste', 'password': 'senha123'})
        # Verifica se o usuário é redirecionado para a página do painel (dashboard)
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_invalid_user(self):
        """
        Testa o login com um nome de usuário inválido.
        """
        # Envia uma requisição POST para a view de login com um nome de usuário inválido e uma senha válida
        response = self.client.post(reverse('login'), {'username': 'usuario_invalido', 'password': 'senha123'})
        # Verifica se a mensagem de erro "Credenciais inválidas" é exibida na resposta
        self.assertContains(response, 'Credenciais inválidas')

    def test_login_invalid_password(self):
        """
        Testa o login com uma senha inválida.
        """
        # Envia uma requisição POST para a view de login com um nome de usuário válido e uma senha inválida
        response = self.client.post(reverse('login'), {'username': 'teste', 'password': 'senha_errada'})
        # Verifica se a mensagem de erro "Credenciais inválidas" é exibida na resposta
        self.assertContains(response, 'Credenciais inválidas')

    def test_login_empty_fields(self):
        """
        Testa o login com campos vazios.
        """
        # Envia uma requisição POST para a view de login sem fornecer nome de usuário ou senha
        response = self.client.post(reverse('login'), {'username': '', 'password': ''})
        # Verifica se a mensagem de erro "Credenciais inválidas" é exibida na resposta
        self.assertContains(response, 'Credenciais inválidas')

    def test_register_duplicate_username(self):
        """
        Testa o registro de um usuário com um nome de usuário duplicado.
        """
        # Envia uma requisição POST para a view de registro com o nome de usuário "teste" e outros dados válidos
        response = self.client.post(reverse('register'), {
            'username': 'teste',
            'email': 'novo@example.com',
            'password1': 'nova_senha',
            'password2': 'nova_senha'
        })
        # Verifica se a mensagem de erro "Usuário já existe" é exibida na resposta
        self.assertContains(response, 'Usuário já existe')
        # Verifica se apenas um usuário com o nome de usuário "teste" existe no banco de dados
        self.assertEqual(get_user_model().objects.filter(username='teste').count(), 1)