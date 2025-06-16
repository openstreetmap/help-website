+++
type = "question"
title = "How to put a query  in a single line to invoke from a script?"
description = '''Hi, I made a query that does what I want, http://overpass-turbo.eu/s/e97  but I found no info on how to put in a single to invoke from a script like wget &amp;lt;query&amp;gt;. Any help is welcomed.'''
date = "2016-02-02T19:51:00Z"
lastmod = "2016-02-03T07:09:00Z"
weight = 47822
keywords = [ "overpass", "invoking", "command", "script" ]
aliases = [ "/questions/47822" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to put a query in a single line to invoke from a script?](/questions/47822/how-to-put-a-query-in-a-single-line-to-invoke-from-a-script)

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
<span id="post-47822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47822-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I made a query that does what I want, <a href="http://overpass-turbo.eu/s/e97">http://overpass-turbo.eu/s/e97</a> but I found no info on how to put in a single to invoke from a script like wget &lt;query&gt;. Any help is welcomed.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-invoking" rel="tag" title="see questions tagged &#39;invoking&#39;">invoking</span> <span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '16, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/772cf5e19ede26c5fc7fcef9af6259b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davide_ttk&#39;s gravatar image" />
<p><span>davide_ttk</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davide_ttk has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '16, 20:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47822" class="comments-container">
&#10;</div>
<div id="comment-tools-47822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47822-form-container" class="comment-form-container">
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

<span id="47824"></span>

<div id="answer-container-47824" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47824-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-47824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>In overpass turbo run your query.</li>
<li>Click on export button and choose raw data from overpass api.</li>
<li>Use the url of the page you landed on for wget.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '16, 20:34</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-47824" class="comments-container">
&#10;</div>
<div id="comment-tools-47824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47824-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47826"></span>

<div id="answer-container-47826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47826-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try to use Overpass API</p>
<p>wiki page: [1]: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
<p>site page: <a href="http://overpass-api.de/">http://overpass-api.de/</a></p>
<p>and for a page that explain how to use it from a command line (or in your case from a script) see this page: <a href="http://overpass-api.de/command_line.html">http://overpass-api.de/command_line.html</a></p>
<p>Please note this two point:</p>
<p>1) the main server has an usage policy (see the wiki page about that)</p>
<p>2) the syntax used by Overpass api may be different from the one used by Overpass Turbo (I am not sure about this, there are two many languages used, I get confused)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '16, 20:41</strong></p>
<img src="https://secure.gravatar.com/avatar/2c370d6199fdd6ee986e81f5baa62d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AnyFile&#39;s gravatar image" />
<p><span>AnyFile</span><br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AnyFile has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47826" class="comments-container">
<span id="47834"></span>
<div id="comment-47834" class="comment">
<div id="post-47834-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks AnyFile it was exactly what I needed</p>
</div>
<div id="comment-47834-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 22:20)</span> <span class="comment-user userinfo">davide_ttk</span>
</div>
</div>
</div>
<div id="comment-tools-47826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47826-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47843"></span>

<div id="answer-container-47843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Remove comments and newlines. You should get something like this:</p>
<p><code>[out:json][timeout:25];(node (poly: "45.5 11 45.6 11.6 45.2 11")["natural"="peak"];);out body;&gt;;out skel qt;</code></p>
<p><code>urlencode</code> that string. You can use this <a href="http://meyerweb.com/eric/tools/dencoder/">http://meyerweb.com/eric/tools/dencoder/</a> or any other tool for urlencode.</p>
<p>Get the encoded string and slap it in wget:</p>
<p><code>wget -O result.json "http://overpass.osm.rambler.ru/cgi/interpreter?data=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B(node%20(poly%3A%20%2245.5%2011%2045.6%2011.6%2045.2%2011%22)%5B%22natural%22%3D%22peak%22%5D%3B)%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B"</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '16, 07:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-47843" class="comments-container">
&#10;</div>
<div id="comment-tools-47843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47843-form-container" class="comment-form-container">
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

