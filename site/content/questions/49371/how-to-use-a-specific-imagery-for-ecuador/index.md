+++
type = "question"
title = "How to use a specific imagery for Ecuador"
description = '''I want to collaborate in the Ecuador tasks. In HOT (http://tasks.hotosm.org/project/1839#task/209), they say we have to use a imagery with the following link: tms[22]:http://imagery.openstreetmap.fr/tms/1.0.0/ecuador_sigtierras_jama/{zoom}/{x}/{y}  However, the link is not valid. I have to delete th...'''
date = "2016-04-23T05:08:00Z"
lastmod = "2016-04-23T06:35:00Z"
weight = 49371
keywords = [ "url", "josm", "imagery" ]
aliases = [ "/questions/49371" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use a specific imagery for Ecuador](/questions/49371/how-to-use-a-specific-imagery-for-ecuador)

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
<span id="post-49371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49371-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to collaborate in the Ecuador tasks. In HOT (<a href="http://tasks.hotosm.org/project/1839#task/209),">http://tasks.hotosm.org/project/1839#task/209),</a> they say we have to use a imagery with the following link:</p>
<pre><code>tms[22]:http://imagery.openstreetmap.fr/tms/1.0.0/ecuador_sigtierras_jama/{zoom}/{x}/{y}</code></pre>
<p>However, the link is not valid. I have to delete the first part: tms[22]:</p>
<pre><code>http://imagery.openstreetmap.fr/tms/1.0.0/ecuador_sigtierras_jama/{zoom}/{x}/{y}</code></pre>
<p>Once the URL is like the following, I can do get layers in JOSM&gt;Imagery preference. Finally, I selected the Equator_sigtierras_jama and I click ok.</p>
<p>When I try to use the imagery, JOSM returns the following message:</p>
<pre><code>{zoom} is not a valid WMS argument. Please check this server URL.</code></pre>
<p>What am I doing wrong? how should I use the URL to use the proposed imagery?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '16, 05:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6998587ec6de0bab814c70777bcdd2ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AngocA&#39;s gravatar image" />
<p><span>AngocA</span><br />
<span class="score" title="281 reputation points">281</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AngocA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '16, 14:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-49371" class="comments-container">
&#10;</div>
<div id="comment-tools-49371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49371-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="49374"></span>

<div id="answer-container-49374" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49374-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The imagery is TMS, I think you tried to add a WMS (given the error) layer. Press +TMS button, then paste the link (without the tms[22]:) in the URL field.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '16, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-49374" class="comments-container">
&#10;</div>
<div id="comment-tools-49374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49374-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49373"></span>

<div id="answer-container-49373" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49373-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM is expecting the tms[22]: in the tile server description, it gives information about how the imagery is served. Deleting it from the description results in JOSM interpreting the description incorrectly and not making the correct requests to the server.</p>
<p>Usually the tasking manager will tell JOSM about the imagery layer, you shouldn't need to set it up manually. I haven't checked the task, but you could try just using the Tasking Manager remote control link to see if it passes the information about the imagery to JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '16, 06:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '16, 06:18</strong> </span></p>
</div>
</div>
<div id="comments-container-49373" class="comments-container">
&#10;</div>
<div id="comment-tools-49373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49373-form-container" class="comment-form-container">
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

