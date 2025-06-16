+++
type = "question"
title = "How much RAM does osm2pgsql required in case  the progress won&#x27;t be killed?  (full planet import)"
description = '''I have 20GB RAM and I have allocated 22GB swap to cater for the planet.osm data. My shell command on the Ubuntu14.04 like this  osm2pgsql -dosmgis -s -S&quot;./default.style&quot; -C16384 -Uwww-data -W -Hlocalhost -v ~/planet-140625.osm.bz2 the import time is too long with the speed (nodes=88k/s ways=0.15k/s,...'''
date = "2014-12-07T04:46:00Z"
lastmod = "2014-12-09T00:39:00Z"
weight = 39111
keywords = [ "import", "ram", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/39111" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How much RAM does osm2pgsql required in case the progress won't be killed? (full planet import)](/questions/39111/how-much-ram-does-osm2pgsql-required-in-case-the-progress-wont-be-killed-full-planet-import)

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
<span id="post-39111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39111-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have 20GB RAM and I have allocated 22GB swap to cater for the planet.osm data. My shell command on the Ubuntu14.04 like this osm2pgsql -dosmgis -s -S"./default.style" -C16384 -Uwww-data -W -Hlocalhost -v ~/planet-140625.osm.bz2 the import time is too long with the speed (nodes=88k/s ways=0.15k/s,rels=11.2/s) and the nodes,ways and rels have been read in for about 1 week</p>
<p>but when the process move to "Committing transaction for planet_osm_point" it show "There is no transaction in progress" after I check the "dmesg" it shows "Out of memory kill osm2pgsql" so what I can do to deal with this proble? someone can give me some advices? with many thanks!!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-ram" rel="tag" title="see questions tagged &#39;ram&#39;">ram</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '14, 04:46</strong></p>
<img src="https://secure.gravatar.com/avatar/841114de2d314468981bc74e8ae743ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="studiousdavid&#39;s gravatar image" />
<p><span>studiousdavid</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="studiousdavid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '14, 10:52</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-39111" class="comments-container">
<span id="39114"></span>
<div id="comment-39114" class="comment">
<div id="post-39114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi why do you ask the same related question after one hour again ? Duplicated questions tend to be closed without answering !</p>
</div>
<div id="comment-39114-info" class="comment-info">
<span class="comment-age">(07 Dec '14, 11:47)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="39115"></span>
<div id="comment-39115" class="comment">
<div id="post-39115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3443/hendrikklaas">@Hendrikklaas</a> It's a different question</p>
</div>
<div id="comment-39115-info" class="comment-info">
<span class="comment-age">(07 Dec '14, 11:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39111-form-container" class="comment-form-container">
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

<span id="39147"></span>

<div id="answer-container-39147" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39147-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just ran an import and on first try ran in to similar problems (and I have a lot of imports under my belt), but that is normal, OSM data continues to grow at a rapid pace and the tools are evolving too.</p>
<p>First you should be setting -C to 25000, then you will need to allocate more swap. On my machine with 32GB RAB it peaked at 24GB, I would aim for a total of 40-50GB swap to be on the safe side.</p>
<p>Note: if you are using a current osm2pgsql you shoud likely not use multiple processes if you are using the persistent node cache.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '14, 00:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Dec '14, 00:24</strong> </span></p>
</div>
</div>
<div id="comments-container-39147" class="comments-container">
<span id="39149"></span>
<div id="comment-39149" class="comment">
<div id="post-39149-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for sharing your expriences!</p>
</div>
<div id="comment-39149-info" class="comment-info">
<span class="comment-age">(09 Dec '14, 00:39)</span> <span class="comment-user userinfo">studiousdavid</span>
</div>
</div>
</div>
<div id="comment-tools-39147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39147-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="39113"></span>

<div id="answer-container-39113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi studiousdavid, welcome, you might or please read this <a href="/questions/12318/why-is-my-import-of-planet-latestosm-killed">https://help.openstreetmap.org/questions/12318/why-is-my-import-of-planet-latestosm-killed</a> and other import related questions. Just by adding import or osm2pgsql into the blank line above.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '14, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-39113" class="comments-container">
<span id="39148"></span>
<div id="comment-39148" class="comment">
<div id="post-39148-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Hendrikklaas! I have read some of the FQA but I'm still a little bit confused</p>
</div>
<div id="comment-39148-info" class="comment-info">
<span class="comment-age">(09 Dec '14, 00:38)</span> <span class="comment-user userinfo">studiousdavid</span>
</div>
</div>
</div>
<div id="comment-tools-39113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39113-form-container" class="comment-form-container">
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

