+++
type = "question"
title = "Interdiction de tourner sur entree/sortie de rond-point"
description = '''Dans une problématique de calcul d&#x27;itinéraire et à des fins de normalisation de règles de création, ne faudrait-il pas avertir le contributeur de positionner les interdiction de tourner à gauche sur les entrées/sorties de rond-point. De la même façon, ne faudrait-il ajouter comme règle de modélisati...'''
date = "2012-07-02T10:53:00Z"
lastmod = "2012-07-03T10:14:00Z"
weight = 13939
keywords = [ "turn_restrictions", "roundabout", "french" ]
aliases = [ "/questions/13939" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interdiction de tourner sur entree/sortie de rond-point](/questions/13939/interdiction-de-tourner-sur-entreesortie-de-rond-point)

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
<span id="post-13939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13939-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dans une problématique de calcul d'itinéraire et à des fins de normalisation de règles de création, ne faudrait-il pas avertir le contributeur de positionner les interdiction de tourner à gauche sur les entrées/sorties de rond-point. De la même façon, ne faudrait-il ajouter comme règle de modélisation pour OSMOSE ce cas particulier pour les détecter ? Merci</p>
<p>Ci-joint un calcul d'itinéraire pour expliquer ma requête.</p>
<p><a href="http://map.project-osrm.org/Nh">Calcul d'itinéraire sur OSRM</a></p>
<p>Pour plus de précisions dans la question:</p>
<p>1°) il ne s'agit pas de la définition du rond-point et du sens de circulation</p>
<p>2°) Il ne s'agit pas de la distinction entre un sens giratoire et un rond-point et la différence dans les règles de propriétés</p>
<p>3°) Il ne s'agit pas de l'absence ou de la présence de tags SUR le rond-point.</p>
<p>M'enfin, rien ne vous choque ?</p>
<p><strong>Il est absolument impossible dans la réalité de sortir d'un rond-point et d'immédiatement reprendre la voie opposée pour y re-rentrer.</strong> Sur le lien "calcul d'itinéraire sur OSRM" on peut voir cette <strong>manoeuvre rigoureusement interdite par la sécurité routière</strong>.</p>
<p>Depuis le point de départ (sur un segment en sortie de rond-point) on repart sur le rond-point pour reprendre une voie d'entrée sur le rond-point. Je parle de ce noeud de liaison entre entrée/sortie qui ne porte pas de restriction "Interdit de tourner à gauche" et qui permet ce calcul d'itinéraire incorrect. Ici, il y a franchissement d'une ligne blanche continue.</p>
<p>Je ne parle que des carrefours de type "Rond-point" ayant une configuration de segments entrée/sortie dédoublée créant une sorte de "bifide" (sous ce genre de représentation "&lt;".</p>
<p>Le segment sortie de rond-point et le segment entrée du rond-point constituant un angle.</p>
<p>A la jonction de ces deux segments, le noeud (qui représente la pointe de ce triangle) devrait être taggé par une restriction d'interdiction de tourner à gauche car dans la réalité il est interdit de le faire car cela constitue une manoeuvre interdite.</p>
<p>Suivant la taille des rond-points d'ailleurs on a des zébras ou des îlots ou au minimum une bande blanche après cette pointe.</p>
<p>Rien ne me manque car la création d'une interdiction de tourner à gauche sur le noeud suffit. Cependant, je suggère (à concurrence de l'adhésion de la communauté à cette idée) que cela soit pris en compte comme une règle de modélisation.</p>
<p>Si vous considérez que l'usager peut se permettre ce genre de manoeuvre alors... Je vous conseille d'afficher une orthophoto voir une photo aérienne pour comprendre ce que je vous signale. (affichez Bing aerial depuis OSRM en utilisant le lien)</p>
<p>Merci.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span> <span class="post-tag tag-link-french" rel="tag" title="see questions tagged &#39;french&#39;">french</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jul '12, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/b28ca8ba2441402a0b89d506b036ca91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DOM91&#39;s gravatar image" />
<p><span>DOM91</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DOM91 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '12, 09:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-13939" class="comments-container">
<span id="13956"></span>
<div id="comment-13956" class="comment">
<div id="post-13956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ta question n'a rien à voir avec les carrefours eux-même mais tout à voir avec les lignes continues (le titre de ta question est trompeur). Est-ce que tu veux dire qu'il est toujours interdit de faire demi-tour à la sortie d'un rond-point ou est-ce que c'est interdit uniquement s'il y a une ligne blanche ? Il m'arrive de faire demi-tour si je prend la mauvaise sortie et s'il n'y a aucune ligne blanche continue (ce qui est le cas dans les petits ronds-points). Est-ce alors interdit ? Non. En fait, ce qui te manque, c'est de tagguer la ligne continue et sa distance d'application, non ?</p>
</div>
<div id="comment-13956-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 09:20)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="13958"></span>
<div id="comment-13958" class="comment">
<div id="post-13958-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Prend l'habitude d'éditer ta question si tu ajoutes des détails. Ce site n'est pas un forum de discussion mais un site de 1 question par page + des réponses. Les forums sont ailleurs (voir la page wiki Fr:Contact)</p>
</div>
<div id="comment-13958-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 09:42)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="13959"></span>
<div id="comment-13959" class="comment">
<div id="post-13959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, désolé.</p>
</div>
<div id="comment-13959-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 09:44)</span> <span class="comment-user userinfo">DOM91</span>
</div>
</div>
<span id="13961"></span>
<div id="comment-13961" class="comment">
<div id="post-13961-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Non, y a pas. La question est légitime mais il n'existe pas actuellement de modélisation très répandue des lignes blanches continues dans OSM (c'est probablement quelque chose qui viendra avec le temps).</p>
</div>
<div id="comment-13961-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 10:08)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-13939" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13939-form-container" class="comment-form-container">
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

<span id="13960"></span>

<div id="answer-container-13960" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13960-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On ne peut pas modéliser une interdiction systématique de tourner à gauche sur ce noeud (&gt;-). Comme dit, dans la réalité, ces limitations peuvent grandement varier d'une intersection à l'autre. S'il y a une ligne continue ou des zebras, cela peut être sur quelques mètres ou des centaines de mètres, 50 centimètres ou ... pas du tout. Il est impossible qu'un outil de détection comme Osmose puisse savoir s'il y a une erreur ou pas.</p>
<p>Par contre, on peut modéliser cette interdiction de franchissement symbolisée au sol par un zebra ou une ligne continue. Placer une relation de type "<a href="http://wiki.openstreetmap.org/wiki/Relation:restriction">interdiction de tourner à gauche</a>" n'est, amha, pas très productif car il n'indique pas à un routeur à partir de quel point on peut faire réellement demi-tour. Il serait plus intelligent de tagguer la portion de route qui a une ligne continue en la coupant en deux pour qu'on puisse voir à quel endroit la ligne continue s'arrête (une proposition de tag existe sur le wiki ("<a href="http://wiki.openstreetmap.org/wiki/Proposed_features/Divided_road">divider=line ou legal</a>") mais n'est pas très utilisée actuellement <a href="http://taginfo.openstreetmap.org/keys/divider#values">d'après les statistiques</a>) et il y a fort peu de chance qu'il soit pris en compte dans OSRM pour l'instant).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '12, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '12, 10:01</strong> </span></p>
</div>
</div>
<div id="comments-container-13960" class="comments-container">
<span id="13963"></span>
<div id="comment-13963" class="comment">
<div id="post-13963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, je comprend.</p>
</div>
<div id="comment-13963-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 10:14)</span> <span class="comment-user userinfo">DOM91</span>
</div>
</div>
</div>
<div id="comment-tools-13960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13960-form-container" class="comment-form-container">
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

