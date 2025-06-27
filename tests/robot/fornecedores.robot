*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://localhost:5000/suppliers    chrome    options=${CHROME_OPTIONS}
Suite Teardown    Close Browser

Suite Setup    Create Directory    screenshots
Test Teardown    Capture Page Screenshot    screenshots/${TEST NAME}.png
*** Test Cases ***
Adicionar Fornecedor
    Click Link    xpath=//a[contains(text(),"Adicionar Fornecedor")]
    Input Text    id=name    Fornecedor Teste
    Click Button    xpath=//button[@type="submit" and contains(text(),"Salvar")]
    Wait Until Page Contains    Fornecedor Teste    timeout=5s

Editar Fornecedor
    Click Link    xpath=//tr[td[contains(text(),"Fornecedor Teste")]]//a[contains(text(),"Editar")]
    Input Text    id=name    Fornecedor Teste Editado
    Click Button    xpath=//button[@type="submit" and contains(text(),"Atualizar")]
    

Excluir Fornecedor
    Click Button    xpath=//tr[td[contains(text(),"Fornecedor Teste Editado")]]//form/button[contains(text(),"Deletar")]
    Handle Alert    ACCEPT
    
