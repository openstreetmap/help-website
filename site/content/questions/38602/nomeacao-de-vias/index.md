+++
type = "question"
title = "Nomeação de vias"
description = '''Estou trabalhando na nomeação de vias e tenho dúvidas quanto a forma correta de atribuição do nome da via, quando se refere à nome de bloco ou conjunto em pares e também números ordinais, conforme exemplos:  Blocos 110 e 120 ou Blocos 110 / 120, ou ambos? Segunda Avenida ou 2ª Avenida, ou ambos?  Pe...'''
date = "2014-11-16T17:10:00Z"
lastmod = "2014-11-19T10:47:00Z"
weight = 38602
keywords = [ "lang-pt", "vias", "nomes" ]
aliases = [ "/questions/38602" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nomeação de vias](/questions/38602/nomeacao-de-vias)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Estou trabalhando na nomeação de vias e tenho dúvidas quanto a forma correta de atribuição do nome da via, quando se refere à nome de bloco ou conjunto em pares e também números ordinais, conforme exemplos:</p>
<ol>
<li>Blocos 110 e 120 ou Blocos 110 / 120, ou ambos?</li>
<li>Segunda Avenida ou 2ª Avenida, ou ambos?</li>
</ol>
<p>Peço ainda, se possível, informar em que se baseia o argumento (alguma norma do OSM) para que seja feito dessa forma. Senão tiver tudo bem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lang-pt" rel="tag" title="see questions tagged &#39;lang-pt&#39;">lang-pt</span> <span class="post-tag tag-link-vias" rel="tag" title="see questions tagged &#39;vias&#39;">vias</span> <span class="post-tag tag-link-nomes" rel="tag" title="see questions tagged &#39;nomes&#39;">nomes</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '14, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/62b0db5708737186a53757d471a515ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seth&#39;s gravatar image" />
<p><span>seth</span><br />
<span class="score" title="201 reputation points">201</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '14, 17:31</strong> </span></p>
</div>
</div>
<div id="comments-container-38602" class="comments-container">
&#10;</div>
<div id="comment-tools-38602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38602-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38624"></span>

<div id="answer-container-38624" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38624-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="seth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>Acho que tanto faz, embora seja interessante que a cidade siga um padrão.</li>
<li>Por extenso. Mas pode ser uma boa ideia adicionar uma tag <code>alt_name</code> com o valor numérico. Por exemplo: <a href="http://www.openstreetmap.org/way/291689173">http://www.openstreetmap.org/way/291689173</a></li>
</ol>
<p>A exceção para esse argumento seria ruas com numeração muito alta, <em>na minha opinião</em>. "Rua Cento e Vinte e Três" ia ficar meio ilegível no mapa. Nesse caso, eu colocaria <code>name=Rua 123</code> e <code>alt_name=Rua Cento e Vinte e Três</code>. De qualquer maneira é importante ter a versão abreviada e a versão por extenso para que o sistema aceite buscas das duas formas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '14, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/673ca6641412c68c138afd1ba8bda156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nighto&#39;s gravatar image" />
<p><span>Nighto</span><br />
<span class="score" title="196 reputation points">196</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nighto has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-38624" class="comments-container">
<span id="38633"></span>
<div id="comment-38633" class="comment">
<div id="post-38633-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nighto, ok quanto ao item 2. Mas o item 1 persiste:<br />
1- Os blocos são numéricos mesmo.<br />
2- De um lado é (por exemplo) bloco 10 e do outro 20.<br />
3- Como é uma via, tenho que indicar ambos.<br />
4- Uso "e" ou "/"?<br />
</p>
</div>
<div id="comment-38633-info" class="comment-info">
<span class="comment-age">(17 Nov '14, 20:44)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
<span id="38637"></span>
<div id="comment-38637" class="comment">
<div id="post-38637-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>seth, não tenho uma resposta pronta, mas olhando o mapa de Brasília (por exemplo: <a href="http://www.openstreetmap.org/#map=17/-15.80632/-47.89408">http://www.openstreetmap.org/#map=17/-15.80632/-47.89408</a> ) posso ver que os mapeadores de lá adotaram a convenção <code>Nome 123/456</code> e <code>Nome1 123 / Nome2 456</code> para indicar as vias (que na verdade não tem nome, apenas os blocos são nomeados). Dessa forma, seguindo o exemplo, seria <code>Blocos 110/120</code>.</p>
</div>
<div id="comment-38637-info" class="comment-info">
<span class="comment-age">(17 Nov '14, 23:24)</span> <span class="comment-user userinfo">Nighto</span>
</div>
</div>
<span id="38661"></span>
<div id="comment-38661" class="comment">
<div id="post-38661-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nighto, no caso de Brasília é mais ou menos isso.<br />
Isso que você falou se aplica à entre quadras e a noeação é exatamente assim: nº/nº. Quando for duas, como no exemplo que dei é que estou em dúvida. No exemplo a via leva o nome dos blocos (de casas).<br />
* Bloco 100 (lado direito) e Bloco 120 (lado esquerdo). * A via é nomeada assim: Blocos 100 e 120. * A minha dúvida é se esse "e" está correto (pelo OSM). Não poderia ser uma "/". * No Google está como "e".</p>
</div>
<div id="comment-38661-info" class="comment-info">
<span class="comment-age">(19 Nov '14, 10:47)</span> <span class="comment-user userinfo">seth</span>
</div>
</div>
</div>
<div id="comment-tools-38624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38624-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

