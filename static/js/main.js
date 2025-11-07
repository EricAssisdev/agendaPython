// Funções JavaScript para a Agenda Eletrônica

// Auto-dismiss de mensagens após 5 segundos
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.fade-in');
    
    messages.forEach(function(message) {
        setTimeout(function() {
            message.classList.add('fade-out');
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 5000);
    });
});

// Confirmação antes de excluir
function confirmDelete(nome) {
    return confirm(`Tem certeza que deseja excluir o contato "${nome}"? Esta ação não pode ser desfeita.`);
}

// Formatação de telefone enquanto digita
function formatPhone(input) {
    let value = input.value.replace(/\D/g, '');
    
    if (value.length <= 10) {
        // Formato: (XX) XXXX-XXXX
        value = value.replace(/^(\d{2})(\d{4})(\d{4}).*/, '($1) $2-$3');
    } else {
        // Formato: (XX) XXXXX-XXXX
        value = value.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
    }
    
    input.value = value;
}

// Adicionar formatação automática aos campos de telefone
document.addEventListener('DOMContentLoaded', function() {
    const phoneInputs = document.querySelectorAll('input[type="text"][name*="telefone"], input[type="text"][name*="celular"]');
    
    phoneInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            formatPhone(this);
        });
    });
});

// Preview de imagem antes do upload
function previewImage(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const preview = document.createElement('img');
            preview.src = e.target.result;
            preview.className = 'mt-3 w-32 h-32 rounded-lg object-cover border-2 border-gray-200';
            
            // Remove preview anterior se existir
            const oldPreview = input.parentElement.querySelector('img.preview');
            if (oldPreview) {
                oldPreview.remove();
            }
            
            preview.classList.add('preview');
            input.parentElement.appendChild(preview);
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

// Adicionar preview de imagem ao campo de foto
document.addEventListener('DOMContentLoaded', function() {
    const fotoInput = document.querySelector('input[type="file"][name="foto"]');
    
    if (fotoInput) {
        fotoInput.addEventListener('change', function() {
            previewImage(this);
        });
    }
});

// Scroll suave para o topo
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Busca em tempo real (debounce)
let searchTimeout;
function liveSearch(input) {
    clearTimeout(searchTimeout);
    
    searchTimeout = setTimeout(function() {
        // Aqui você pode adicionar lógica AJAX para busca em tempo real
        console.log('Buscando:', input.value);
    }, 500);
}

// Adicionar busca em tempo real ao campo de pesquisa
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('input[name="q"]');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            liveSearch(this);
        });
    }
});

// Toggle favorito com animação
function toggleFavorito(elemento) {
    elemento.classList.add('star-pulse');
    
    setTimeout(function() {
        elemento.classList.remove('star-pulse');
    }, 300);
}

// Validação de formulário
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');
    
    requiredFields.forEach(function(field) {
        if (!field.value.trim()) {
            field.classList.add('field-error');
            isValid = false;
        } else {
            field.classList.remove('field-error');
        }
    });
    
    if (!isValid) {
        alert('Por favor, preencha todos os campos obrigatórios.');
    }
    
    return isValid;
}

// Copiar para clipboard
function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(function() {
        // Feedback visual
        const originalHTML = button.innerHTML;
        button.innerHTML = '<i class="fas fa-check"></i> Copiado!';
        button.classList.add('bg-green-500');
        
        setTimeout(function() {
            button.innerHTML = originalHTML;
            button.classList.remove('bg-green-500');
        }, 2000);
    }).catch(function(err) {
        console.error('Erro ao copiar:', err);
    });
}

// Contador de caracteres para campos de texto
function updateCharCount(textarea, maxLength) {
    const charCount = textarea.value.length;
    const counter = textarea.parentElement.querySelector('.char-counter');
    
    if (counter) {
        counter.textContent = `${charCount}/${maxLength}`;
        
        if (charCount > maxLength * 0.9) {
            counter.classList.add('text-red-600');
        } else {
            counter.classList.remove('text-red-600');
        }
    }
}

// Adicionar contadores de caracteres
document.addEventListener('DOMContentLoaded', function() {
    const textareas = document.querySelectorAll('textarea[maxlength]');
    
    textareas.forEach(function(textarea) {
        const maxLength = textarea.getAttribute('maxlength');
        const counter = document.createElement('div');
        counter.className = 'char-counter text-sm text-gray-500 mt-1 text-right';
        counter.textContent = `0/${maxLength}`;
        
        textarea.parentElement.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            updateCharCount(this, maxLength);
        });
    });
});

// Export para CSV (exemplo básico)
function exportToCSV() {
    console.log('Exportando contatos para CSV...');
    // Aqui você implementaria a lógica de exportação
}

// Imprimir página
function printPage() {
    window.print();
}

console.log('Agenda Eletrônica - Scripts carregados com sucesso!');
