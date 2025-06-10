+++
type = "question"
title = "&quot;moving&quot; nominatim db to another machine (avoiding to repeat the indexing process)"
description = '''Hi guys and thank you in advance I have a virtual machine with nominatim and Italian map (about 1gb I don&#x27;t remember). Now I would like to provide this service to another machine (with no big requirements..) and to avoid the indexing process, I was thinking of install nominatim on their machine and ...'''
date = "2015-12-11T14:44:00Z"
lastmod = "2015-12-11T14:44:00Z"
weight = 47097
keywords = [ "nominatim" ]
aliases = [ "/questions/47097" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# ["moving" nominatim db to another machine (avoiding to repeat the indexing process)](/questions/47097/moving-nominatim-db-to-another-machine-avoiding-to-repeat-the-indexing-process)

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
<span id="post-47097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47097-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys and thank you in advance</p>
<p>I have a virtual machine with nominatim and Italian map (about 1gb I don't remember). Now I would like to provide this service to another machine (with no big requirements..) and to avoid the indexing process, I was thinking of install nominatim on their machine and move (copy) the postgres data folder to their postgres Installation. Do you think can it work??</p>
<p>Thanks a lot</p>
<p>Confirmed!!</p>
<p>Sorry if I edit my post so late but I have tried this procedure and it worked perfectly with montecarlo map.</p>
<p>I dump my postgres db (db where I indexed the map) with this command:</p>
<pre><code> pg_dump nominatim &gt; &lt;folder&gt;/dump.sql</code></pre>
<p>Now put this file in the clean machine where you want replicate the service - follow the wiki.guide untill nominatim installation then create nominatim database with command:</p>
<pre><code>CREATE DATABASE nominatim OWNER &lt;user&gt;</code></pre>
<p>Instead of web user create directly apache user (on centos 6.6) with command:</p>
<pre><code> createuser -SDR apache</code></pre>
<p>execute the db restore with command:</p>
<pre><code> psql -d nominatim -f dump.sql</code></pre>
<p>resume the wiki.guide at paragraph "Install service on http" and "iptable configuration"</p>
<p>And thats it!! Maybe could help someone Bye</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '15, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/baa53b81d8a54ef27c893d8bc1c4ea0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="developer_afbnet&#39;s gravatar image" />
<p><span>developer_af...</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="developer_afbnet has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '16, 16:01</strong> </span></p>
</div>
</div>
<div id="comments-container-47097" class="comments-container">
&#10;</div>
<div id="comment-tools-47097" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47097-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

