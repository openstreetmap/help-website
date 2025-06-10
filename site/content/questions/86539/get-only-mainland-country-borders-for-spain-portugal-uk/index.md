+++
type = "question"
title = "Get only mainland country borders for Spain, Portugal, UK"
description = '''Hi there! I have recently tried to extract only mainland country borders for France and the Netherlands to exclude colonies and Atlantic Islands. Using the following Overpass queries respectively: [out:json]; rel[admin_level=3][name=&quot;France métropolitaine&quot;]; out geom; and [out:json]; rel[place=regio...'''
date = "2023-01-18T12:33:00Z"
lastmod = "2023-01-24T12:20:00Z"
weight = 86539
keywords = [ "boundaries", "overpass", "borders", "overpass-turbo" ]
aliases = [ "/questions/86539" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get only mainland country borders for Spain, Portugal, UK](/questions/86539/get-only-mainland-country-borders-for-spain-portugal-uk)

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
<span id="post-86539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there!</p>
<p>I have recently tried to extract only mainland country borders for France and the Netherlands to exclude colonies and Atlantic Islands.</p>
<p>Using the following Overpass queries respectively:</p>
<p><code>[out:json]; rel[admin_level=3][name="France métropolitaine"]; out geom;</code></p>
<p>and</p>
<p><code>[out:json]; rel[place=region][name="Europees Nederland"]; out geom;</code></p>
<p>I have tried to find the same for the following three countries:</p>
<p>UK Spain Portugal</p>
<p>but I can't seem to find a satisfactory relation to exclude e.g. the Azores from Portuguese borders and the canaries from the Spanish one. Has anyone solved this issue before or know how I could extend my search for a solution?</p>
<p>Thank you for the help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '23, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/bd39fa8901794d6ac20ba4faa765d461?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jojojatt&#39;s gravatar image" />
<p><span>jojojatt</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jojojatt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '23, 12:34</strong> </span></p>
</div>
</div>
<div id="comments-container-86539" class="comments-container">
&#10;</div>
<div id="comment-tools-86539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86539-form-container" class="comment-form-container">
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

<span id="86541"></span>

<div id="answer-container-86541" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86541-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For Portugal I haven't found anything better than the "Europe/Lisbon Timezone".</p>
<p>Overpass example:</p>
<pre><code>[out:json];
rel[name=&quot;Fuso Horário da Europa/Lisboa&quot;];
out geom;</code></pre>
<p>Link: <a href="http://overpass-turbo.eu/s/1qhW">http://overpass-turbo.eu/s/1qhW</a></p>
<p>For Spain it would be:</p>
<p>Overpass example:</p>
<pre><code>[out:json];
rel[name=&quot;Zona Horaria de Europa/Madrid&quot;];
out geom;</code></pre>
<p>Link: <a href="http://overpass-turbo.eu/s/1qhX">http://overpass-turbo.eu/s/1qhX</a></p>
<p>but this would include the balearic islands and some tiny islet in the street of Gibraltar (but not the Canary Islands).</p>
<p>Now I don't know if you want the United Kingdom including Northern Island or excluding Northern Island.</p>
<p>If you want it without Northern Ireland and without isles, the mainland body of "Great Britain" comes close:</p>
<p>Overpass example:</p>
<pre><code>[out:json];
rel[name=&quot;Great Britain&quot;];
out geom;</code></pre>
<p>Link: <a href="http://overpass-turbo.eu/s/1qhY">http://overpass-turbo.eu/s/1qhY</a></p>
<p>But then, I'm not sure what you want included and excluded...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '23, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '23, 14:02</strong> </span></p>
</div>
</div>
<div id="comments-container-86541" class="comments-container">
<span id="86559"></span>
<div id="comment-86559" class="comment">
<div id="post-86559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi there,</p>
<p>This is absolutely great. Thank you so much. I guess my main question now would be what search strategy would bring me to this information, I have checked the entire OSM Wiki and map dependencies. The names for such special zones always seem to be in their original language.</p>
<p>Could you share where/how you found this information?</p>
</div>
<div id="comment-86559-info" class="comment-info">
<span class="comment-age">(24 Jan '23, 12:13)</span> <span class="comment-user userinfo">jojojatt</span>
</div>
</div>
<span id="86560"></span>
<div id="comment-86560" class="comment">
<div id="post-86560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I'm actually not finding those through Overpass, but by thinking/guessing and using Nominatim. Nominatim is easier as it uses all name (e.g. name, name:en, etc.) fields, so I can search for "Europe/Lisbon timezone" and get a result. Overpass instead would need the exact key (e.g. name or name:en), so it's easier to go the extra mile via Nominatim in finding those objects and then using them in Overpass.</p>
</div>
<div id="comment-86560-info" class="comment-info">
<span class="comment-age">(24 Jan '23, 12:20)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-86541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86541-form-container" class="comment-form-container">
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

