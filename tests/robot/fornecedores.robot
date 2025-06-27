*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://localhost:5000/suppliers    chrome    options=${ENV.ROBOT_CHROME_OPTIONS}
Suite Teardown    Close Browser

*** Test Cases ***
Adicionar Fornecedor
    Click Link    xpath=//a[contains(text(),"Adicionar Fornecedor")]
    Input Text    id=name    Fornecedor Teste
    Click Button    xpath=//button[@type="submit" and contains(text(),"Salvar")]
    Page Should Contain    Fornecedor Teste

Editar Fornecedor
    Click Link    xpath=//tr[td[contains(text(),"Fornecedor Teste")]]//a[contains(text(),"Editar")]
    Input Text    id=name    Fornecedor Teste Editado
    Click Button    xpath=//button[@type="submit" and contains(text(),"Atualizar")]
    Page Should Contain    Fornecedor Teste Editado

Excluir Fornecedor
    Click Button    xpath=//tr[td[contains(text(),"Fornecedor Teste Editado")]]//form/button[contains(text(),"Deletar")]
    Handle Alert    ACCEPT
    Page Should Not Contain    Fornecedor Teste Editado
