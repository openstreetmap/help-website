+++
type = "question"
title = "./utils/setup.php: No such file or directory initial data"
description = '''Hello friends ! I&#x27;m new here in the forum and am trying to install my first Nominatim server. I need it to reverse geocode . I am following the step by step installation manual as in : https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS . and I am facing the following problem on the ...'''
date = "2015-09-23T20:10:00Z"
lastmod = "2015-09-24T07:46:00Z"
weight = 45532
keywords = [ "postgresql", "initial", "installation", "nominatim" ]
aliases = [ "/questions/45532" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [./utils/setup.php: No such file or directory initial data](/questions/45532/utilssetupphp-no-such-file-or-directory-initial-data)

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
<span id="post-45532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45532-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello friends !</p>
<p>I'm new here in the forum and am trying to install my first Nominatim server.</p>
<p>I need it to reverse geocode . I am following the step by step installation manual as in : <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS">https://wiki.openstreetmap.org/wiki/Nominatim/Installation_on_CentOS</a> . and I am facing the following problem on the orientation of import initial data.</p>
<p>I ran the following command:</p>
<pre><code>./utils/setup.php --osm-file brazil-latest.osm.pbf --all --osm2pgsql-cache 18000</code></pre>
<p>But returns as follows:</p>
<pre><code>./utils/setup.php: No such file or directory</code></pre>
<p>Already researched corrections but so far not found , I thank if anyone can help me .</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-initial" rel="tag" title="see questions tagged &#39;initial&#39;">initial</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '15, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/5950462743c0b01abaa4f4c9dfc3eff4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wmarth&#39;s gravatar image" />
<p><span>wmarth</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wmarth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '15, 06:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45532" class="comments-container">
<span id="45540"></span>
<div id="comment-45540" class="comment">
<div id="post-45540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do not know if made ​​properly, but after its review performed the procedure below and it was the same result , EVEN knowing que la Within this setup.php . See:</p>
<pre><code>[root@nominaticentos /]# cd /srv/Nominatim/utils
[root@nominaticentos utils]# ./utils/setup.php --osm-file brazil-latest.osm.pbf  --all --osm2pgsql-cache 18000 2&gt;&amp;1 | tee setup.log
-bash: ./utils/setup.php: No such file or directory</code></pre>
</div>
<div id="comment-45540-info" class="comment-info">
<span class="comment-age">(24 Sep '15, 01:36)</span> <span class="comment-user userinfo">wmarth</span>
</div>
</div>
<span id="45552"></span>
<div id="comment-45552" class="comment">
<div id="post-45552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you already switched to the <code>utils</code> directory then remove <code>/utils</code> from the call and just run <code>./setup.php [...]</code> instead. Alternatively just run <code>cd /srv/Nominatim/</code>.</p>
</div>
<div id="comment-45552-info" class="comment-info">
<span class="comment-age">(24 Sep '15, 07:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45532-form-container" class="comment-form-container">
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

<span id="45536"></span>

<div id="answer-container-45536" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45536-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you in the correct directory? After unpacking the tar archive or cloning the git directory you should switch to the newly created Nominatim directory where <code>./utils/setup.php</code> should be located.</p>
<p>Based on your new comment: After you did <code>cd /srv/Nominatim/utils</code> you already are in the utils directiory. If you try to run <code>./utils/setup.php</code> you are actually trying to run the file <code>/srv/Nominatim/utils/utils/setup.php</code> – and this file does not exist.</p>
<p>So, try this:</p>
<pre><code>[root@nominaticentos /]# cd /srv/Nominatim
[root@nominaticentos Nominatim]# ./utils/setup.php --osm-file brazil-latest.osm.pbf  --all --osm2pgsql-cache 18000 2&gt;&amp;1 | tee setup.log</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '15, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Sep '15, 06:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45536" class="comments-container">
&#10;</div>
<div id="comment-tools-45536" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45536-form-container" class="comment-form-container">
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

