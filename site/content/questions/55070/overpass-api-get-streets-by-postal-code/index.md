+++
type = "question"
title = "Overpass API: Get streets by postal code"
description = '''I want to get every street in a postal code area, my code works fine for Germany  [out:csv(name;false)]; area[postal_code=&quot;10115&quot;]-&amp;gt;.a; way(area.a)[highway][name]; out;  But how can I query for other countries with postal code system? For example FIN or CH? Thanks a lot :)'''
date = "2017-03-14T18:33:00Z"
lastmod = "2017-05-24T15:01:00Z"
weight = 55070
keywords = [ "overpass", "overpass-turbo" ]
aliases = [ "/questions/55070" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Get streets by postal code](/questions/55070/overpass-api-get-streets-by-postal-code)

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
<span id="post-55070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get every street in a postal code area, my code works fine for Germany</p>
<pre><code> [out:csv(name;false)];
area[postal_code=&quot;10115&quot;]-&gt;.a;
way(area.a)[highway][name];
out;</code></pre>
<p>But how can I query for other countries with postal code system? For example FIN or CH?</p>
<p>Thanks a lot :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '17, 18:33</strong></p>
<img src="https://secure.gravatar.com/avatar/82c9cb7fa0aa3401bc4c557289a2dfad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kampfkeks18&#39;s gravatar image" />
<p><span>kampfkeks18</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kampfkeks18 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55070" class="comments-container">
<span id="55100"></span>
<div id="comment-55100" class="comment">
<div id="post-55100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/232041/query-all-streets-by-postal-code-overpass-turbo-api">https://gis.stackexchange.com/questions/232041/query-all-streets-by-postal-code-overpass-turbo-api</a></p>
</div>
<div id="comment-55100-info" class="comment-info">
<span class="comment-age">(15 Mar '17, 07:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56286"></span>
<div id="comment-56286" class="comment">
<div id="post-56286-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think your query is incorrect as soon as there is another region somewhere in the world that also has postal code 10115.</p>
</div>
<div id="comment-56286-info" class="comment-info">
<span class="comment-age">(24 May '17, 15:01)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-55070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55070-form-container" class="comment-form-container">
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

<span id="56280"></span>

<div id="answer-container-56280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56280-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the closest you can get without having postal_code areas defined is:</p>
<pre><code>[out:json][timeout:25];
// fetch area “Polska” to search in
{{geocodeArea:Polska}}-&gt;.searchArea;
// gather results
(
  node[&quot;addr:postcode&quot;=&quot;04-035&quot;](area.searchArea);
  way[&quot;addr:postcode&quot;=&quot;04-035&quot;](area.searchArea);
  relation[&quot;addr:postcode&quot;=&quot;04-035&quot;](area.searchArea);
)-&gt;.addr;
way[&quot;highway&quot;][&quot;name&quot;](around.addr:20.0);
out body;
&gt;;
out skel qt;</code></pre>
<p>But it's not ideal, as far as I know no address at Ostrobramska has postal code 04-035. You may try to change the radius at around.addr: to smaller than 20.0 metres</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '17, 12:16</strong></p>
<img src="https://secure.gravatar.com/avatar/acefea27bc87283a5822bd488404b254?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rmikke&#39;s gravatar image" />
<p><span>rmikke</span><br />
<span class="score" title="15 reputation points">15</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rmikke has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '17, 12:21</strong> </span></p>
</div>
</div>
<div id="comments-container-56280" class="comments-container">
&#10;</div>
<div id="comment-tools-56280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56280-form-container" class="comment-form-container">
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

