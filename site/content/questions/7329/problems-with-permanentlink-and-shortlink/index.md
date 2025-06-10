+++
type = "question"
title = "Problems with Permanentlink and shortlink"
description = '''I am trying to make a Permanentlink and Shortlink. But it doesn&#x27;t work. If I click on the Links nothing happens. Are there any general problems? In german: Ich versuche einen Permanentlink bzw. einen Shortlink zu erstellen. Aber es funktioniert nicht. Beim Klick auf die Links auf der Karte passiert ...'''
date = "2011-08-26T08:29:00Z"
lastmod = "2011-08-26T10:55:00Z"
weight = 7329
keywords = [ "permanentlink" ]
aliases = [ "/questions/7329" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Problems with Permanentlink and shortlink](/questions/7329/problems-with-permanentlink-and-shortlink)

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
<span id="post-7329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7329-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to make a Permanentlink and Shortlink. But it doesn't work. If I click on the Links nothing happens. Are there any general problems?</p>
<p>In german: Ich versuche einen Permanentlink bzw. einen Shortlink zu erstellen. Aber es funktioniert nicht. Beim Klick auf die Links auf der Karte passiert gar nicht. Ist das ein generelles Problem?</p>
<p>Thx Tom</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-permanentlink" rel="tag" title="see questions tagged &#39;permanentlink&#39;">permanentlink</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Aug '11, 08:29</strong></p>
<img src="https://secure.gravatar.com/avatar/5e522cb83155cac3cceb0065bb83c277?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomas_kig&#39;s gravatar image" />
<p><span>thomas_kig</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomas_kig has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7329" class="comments-container">
<span id="7331"></span>
<div id="comment-7331" class="comment">
<div id="post-7331-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Information about what browser you're using and on what platform would be helpful.</p>
</div>
<div id="comment-7331-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 08:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7329" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7329-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="7336"></span>

<div id="answer-container-7336" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7336-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Permalink and shortlink both link to a particular location and zoomlevel in the map, but they are not intended for embedding, what is likely your intention.<br />
Pemanent link is the target for "Größere Karte anzeigen".<br />
</p>
<p>This is taken from the site source code and should be what you need.<br />
</p>
<pre><code>&lt;iframe 
    style=&quot;border-right: black 1px solid; border-top: black 1px solid; border-left: black 1px solid; border-bottom: black 1px solid&quot; 
    marginwidth=&quot;0&quot; 
    marginheight=&quot;0&quot; 
    src=&quot;http://www.openstreetmap.org/export/embed.html?bbox=16.080776,47.718179,16.087101,47.721455&amp;amp;layer=mapnik&amp;amp;marker=47.71984,16.08368&quot; 
    frameborder=&quot;0&quot; width=&quot;350&quot; scrolling=&quot;no&quot; height=&quot;247&quot;&gt;
&lt;/iframe&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '11, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Aug '11, 10:02</strong> </span></p>
</div>
</div>
<div id="comments-container-7336" class="comments-container">
&#10;</div>
<div id="comment-tools-7336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7336-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7334"></span>

<div id="answer-container-7334" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I tried it with Internet Explorer 9.0.8, Chrome 13.0.782.215, Firefox 3.6.8 and Safari 5.1. I tried ist on Windows XP, Windows 7 and OSX Lion. Nothing happens when I am clicking on Permanentlink or on Shortlink. So what shell happen when I am clicking on these Links?</p>
<p>I tried it last week, and it was possible to mark a position and create a html.</p>
<p>I want the same like on this page in the button: <a href="http://www.raiffeisen-neunkirchen.at/eBusiness/rai_template1/491946912887608677-1019074530268_1019074631032-1019074631032-NA-1-NA.html">http://www.raiffeisen-neunkirchen.at/eBusiness/rai_template1/491946912887608677-1019074530268_1019074631032-1019074631032-NA-1-NA.html</a></p>
<p>Or is this another feature?</p>
<p>Thx for help.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '11, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/5e522cb83155cac3cceb0065bb83c277?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomas_kig&#39;s gravatar image" />
<p><span>thomas_kig</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomas_kig has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-7334" class="comments-container">
<span id="7337"></span>
<div id="comment-7337" class="comment">
<div id="post-7337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So if you move the map and click "permalink" it doesn't update the address in the address bar?</p>
</div>
<div id="comment-7337-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 10:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7334-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7339"></span>

<div id="answer-container-7339" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7339-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Oh, now i know, it's in the register export. There I can make the HTML export.</p>
<p>So my question is answered.</p>
<p>Thx a lot.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Aug '11, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/5e522cb83155cac3cceb0065bb83c277?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thomas_kig&#39;s gravatar image" />
<p><span>thomas_kig</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thomas_kig has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7339" class="comments-container">
<span id="7340"></span>
<div id="comment-7340" class="comment">
<div id="post-7340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was thinking in the wrong direction. Sorry.</p>
</div>
<div id="comment-7340-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 10:55)</span> <span class="comment-user userinfo">thomas_kig</span>
</div>
</div>
</div>
<div id="comment-tools-7339" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7339-form-container" class="comment-form-container">
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

