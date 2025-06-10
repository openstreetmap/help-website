+++
type = "question"
title = "Overpass lz4.overpass-api.de endpoint returns a (long) deleted  object"
description = '''An act of vandalism created &quot;Creedon Republic&quot;, a large country object, shown here way/617866825. I put the name of the object here to have my question respond to keyword search.  It was removed on 2018-08-19 with this changeset changeset/61786055. This object is still present in lz4.overpass-api.de...'''
date = "2020-03-23T18:26:00Z"
lastmod = "2020-03-26T21:36:00Z"
weight = 73714
keywords = [ "deleted", "overpass", "lz4" ]
aliases = [ "/questions/73714" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass lz4.overpass-api.de endpoint returns a (long) deleted object](/questions/73714/overpass-lz4overpass-apide-endpoint-returns-a-long-deleted-object)

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
<span id="post-73714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>An act of vandalism created "Creedon Republic", a large country object, shown here <a href="https://www.openstreetmap.org/way/617866825">way/617866825</a>. I put the name of the object here to have my question respond to keyword search.</p>
<p>It was removed on 2018-08-19 with this changeset <a href="https://www.openstreetmap.org/changeset/61786055">changeset/61786055</a>.</p>
<p>This object is still present in lz4.overpass-api.de, but not in other overpass servers.</p>
<p>This command gets the object for me:</p>
<pre><code>wget -O - &quot;http://lz4.overpass-api.de/api/interpreter?data=[out:json];is_in(38.49464,-75.28586);out body;&quot; | more</code></pre>
<p>It looks like this in the results:</p>
<pre><code>... {
      &quot;type&quot;: &quot;area&quot;,
      &quot;id&quot;: 3017866825,
      &quot;tags&quot;: {
        &quot;admin_level&quot;: &quot;1&quot;,
        &quot;boundary&quot;: &quot;administrative&quot;,
        &quot;name&quot;: &quot;Creedon Republic&quot;,
        &quot;place&quot;: &quot;country&quot;
      }
    },...</code></pre>
<p>This one does not:</p>
<pre><code>wget -O - &quot;http://z.overpass-api.de/api/interpreter?data=[out:json];is_in(38.49464,-75.28586);out body;&quot; | more</code></pre>
<p>Is there some misunderstanding on my part as to what the instances are supposed to contain? Or is this a problem with lz4?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deleted" rel="tag" title="see questions tagged &#39;deleted&#39;">deleted</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-lz4" rel="tag" title="see questions tagged &#39;lz4&#39;">lz4</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '20, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/ebf17ea74a0c9e93d1cf657d30e97857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swimdb&#39;s gravatar image" />
<p><span>swimdb</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swimdb has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '20, 23:28</strong> </span></p>
</div>
</div>
<div id="comments-container-73714" class="comments-container">
&#10;</div>
<div id="comment-tools-73714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73714-form-container" class="comment-form-container">
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

<span id="73717"></span>

<div id="answer-container-73717" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73717-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's weird. If I understand the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances">documentation</a>, there should be no differences between those two servers.</p>
<p>One remark is that its type is <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Areas">area</a>, which is a special Overpass type, pre-computed. Maybe something went wrong there.</p>
<p>You should probably raise this issue on the <a href="https://github.com/drolbr/Overpass-API/issues">Overpass repository</a> to touch the servers' maintainers.</p>
<p>This <a href="https://github.com/drolbr/Overpass-API/issues/285">closed issue</a> seems related, especially the last comment.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '20, 02:08</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73717" class="comments-container">
&#10;</div>
<div id="comment-tools-73717" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73717-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73783"></span>

<div id="answer-container-73783" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73783-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After asking over at the <a href="https://github.com/drolbr/Overpass-API/issues/563">overpass help</a>, and there getting more or less the same answer linked to above, I will close this issue.</p>
<p>I am closing it because we respect the decisions of the owners of these systems to "not fix". We do not consider this solved. The lz4 instance is not fit for purpose under these conditions, even with the pivot hack suggested.</p>
<p>Thanks to those who responded.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '20, 21:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ebf17ea74a0c9e93d1cf657d30e97857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swimdb&#39;s gravatar image" />
<p><span>swimdb</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swimdb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73783" class="comments-container">
<span id="73784"></span>
<div id="comment-73784" class="comment">
<div id="post-73784-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, sorry to hear it.</p>
<p>There are other public instances which might have a cleaning policy, and thus suit your needs.</p>
<p>Regards.</p>
</div>
<div id="comment-73784-info" class="comment-info">
<span class="comment-age">(26 Mar '20, 21:36)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73783" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73783-form-container" class="comment-form-container">
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

