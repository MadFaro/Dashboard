class css:
          container_output = """
                              body{
                                font-weight: 1000;
                              }
                              .pywebio{
                                background:white;
                                filter: hue-rotate(346deg);
                                font-family: Svyaznoy Sans Light;}

                              .toastify {
                                font-family: Svyaznoy Sans Light;
                                font-size:0.8vw;
                                }

                              .toastify-right {
                                font-weight: 1000;
                                right: 0px;
                                }

                              .modal-content {
                                font-family: Svyaznoy Sans Light;
                                font-weight: 1000;
                                }

                              .modal-title {
                                font-family: Svyaznoy Sans Light;
                                font-weight: 1000;
                                }

                              .btn-outline-primary {
                                border-color: #dc354500;}

                              .btn-info {
                                border-radius: 1px;
                                border: 0px;
                                filter: drop-shadow(1px 2px 3px #051f23);
                                padding: 0.6vw 1.5vw;
                                font-family: Svyaznoy Sans Light;
                                background-color: #051f23;
                                border-color: #051f23;
                                font-size:0.8vw;
                                font-weight: 1000;
                                line-height: 1.5;
                                }
                                
                              .btn-danger {
                                border-radius: 1px;
                                border: 0px;
                                padding: 0.6vw 1.5vw;
                                font-family: Svyaznoy Sans Light;
                                font-size:0.8vw;
                                font-weight: 1000;
                                line-height: 1.5;
                                background-color: #007ba5;
                                border-color: #007ba5;
                                filter: drop-shadow(1px 2px 3px #007ba5);                        
                                }
                                
                              .card {
                                border-radius: 0px;
                                font-weight: 1000;
                                font-family: Svyaznoy Sans Light;
                                }
                                
                              .toastify-left {
                                font-weight: 1000;
                                left: 0px;
                                }

                              .btn-link{
                                font-size:0.9vw;
				                        color: #000000;
                                padding: 0px 0px;
                                font-weight: 1000;
                                font-family: Svyaznoy Sans Light;}

                              .btn-outline-info {
                                font-size: 1.8vh;
                                font-weight: 1000;
                                filter: hue-rotate(10deg);
                                }

                              .btn-outline-success {
                                ont-size: 1.8vh;
                                font-weight: 1000;
                                filter: hue-rotate(10deg);}

			                        .webio-tabs > input[type=radio]:checked + label {
				                        font-size:0.8vw;
                                font-weight: 1000;
                                border-bottom:0px solid white;}

                              .webio-tabs > input[type=radio]:checked + label:hover {
                                cursor: default;
				                        background:white;}

                              #pywebio-scope-ROOT{
                                color: black;
                                font-size:0.9vw;
                                position: absolute;
                                top: 0;
                                left: 0;
                                width: 100%;
                                height: 100%;}

                              .webio-tabs{
                                position: relative;
                                margin-bottom: 0rem;
                                border: 1px solid #00000014;
                                border-radius: 11px;
                                background: white;
                                box-shadow: 0 0 5px #b7b7b766;
                                transition: all 0.5s ease;}

                              #input-container{
                                background:white;}

                              .progress-bar {
                                white-space: normal;
                                }

                              #img{
                                background: black;
                                position: relative;
                                width: 250%;
                                left: -100%;
                                top: 150%;}

                              table td, table th {
                                border-spacing: 1;
                                background-color: #fff9f908;
                                border: 1px solid #e9ecef;
                                width: 10%;}

                              table{
                                border-spacing: 0;
                                border-collapse: separate;
                              }
                              
                              .markdown-body table td, .markdown-body table th {
                                border-spacing: 1;
                                padding: 6px 13px;
                                border: 1px solid #f3f3f3;}

                              .markdown-body table {
                                border-spacing: 1;
                                border-collapse: separate;
                                box-shadow: 0 0 5px #b7b7b766;}

                              .markdown-body table th {   
                                border-spacing: 1;                  
                                font-weight: 1000;
                                text-align:left;
                                font-size:1vw;}
                                  
                              """

          tpl = '''
          <tab>
              {{#contents}}
                  {{& pywebio_output_parse}}
              {{/contents}}
          </tab>
          '''
          
          img1 = 'https://psv4.vkuseraudio.net/s/v1/d/mn6mFjHa29eX0F7a6_VpG3alSrYpEDl5n12K78QV-3LWsIYxkfSqo3-3vwZmBoyZe3SaK3GEeq9b6OZlmEtL9-6QlIJXJwJ3LT7qNM9WdcDumgejcr37ig/4793010.png'
          img2 = 'https://psv4.userapi.com/c237231/u502607451/docs/d24/6fd052506050/4795042.png?extra=bxruhFyJUzQ25IbajfN0yebJkhA-NYT8VB0UY8PywHSE-XhSOf0QhARSPvv7IUnxlkUnj7nClGzGZQMj596ySeS59V6U5Mtzu2mfNvsi-rKbesuWHkMuKczkHPCyLQFesTIf6qL_TJ-NzMdLuJbWlBIs'