*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://localhost:5000/products    chrome    options=${CHROME_OPTIONS}
Suite Teardown    Close Browser

Suite Setup    Create Directory    screenshots
Test Teardown    Capture Page Screenshot    screenshots/${TEST NAME}.png
*** Test Cases ***
Adicionar Produto
    Click Link    xpath=//a[contains(text(),"Adicionar Produto")]
    Input Text    id=name    Produto Teste
    Input Text    id=price    19.99
    Select From List By Value    id=supplier_id    1
    Click Button    xpath=//button[@type="submit" and contains(text(),"Salvar")]
    Page Should Contain    Produto Teste

Editar Produto
    Click Link    xpath=//tr[td[contains(text(),"Produto Teste")]]//a[contains(text(),"Editar")]
    Input Text    id=name    Produto Teste Editado
    Click Button    xpath=//button[@type="submit" and contains(text(),"Atualizar")]
   

Excluir Produto
    Click Button    xpath=//tr[td[contains(text(),"Produto Teste Editado")]]//form/button[contains(text(),"Deletar")]
    Handle Alert    ACCEPT
    