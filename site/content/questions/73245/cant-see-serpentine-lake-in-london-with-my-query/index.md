+++
type = "question"
title = "Can&#x27;t see Serpentine Lake in London with my query"
description = '''Hi, I&#x27;m running the query: [out:json];  (way[&quot;natural&quot;~&quot;water&quot;] (around:5100.0, 51.508341, -0.125499); ); out meta; &amp;gt;; out skel qt;  To get all the water in Central London, or thereabouts; however, I&#x27;m not seeing any Serpentine Lake and I assume it&#x27;s something to do with it being a multi-polygon....'''
date = "2020-02-26T17:02:00Z"
lastmod = "2020-03-01T10:31:00Z"
weight = 73245
keywords = [ "water", "pond", "lake", "multipolygon" ]
aliases = [ "/questions/73245" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't see Serpentine Lake in London with my query](/questions/73245/cant-see-serpentine-lake-in-london-with-my-query)

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
<span id="post-73245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73245-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm running the query:</p>
<pre><code>[out:json];
&#10;(way[&quot;natural&quot;~&quot;water&quot;] (around:5100.0, 51.508341, -0.125499); ); out meta;
&gt;; out skel qt;</code></pre>
<p>To get all the water in Central London, or thereabouts; however, I'm not seeing any Serpentine Lake and I assume it's something to do with it being a multi-polygon.</p>
<p>Can anyone please assist?</p>
<p>TIA,</p>
<p>Alex</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-pond" rel="tag" title="see questions tagged &#39;pond&#39;">pond</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '20, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/09f53b06dcac1cb83c71c601571cf449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jusdespommes&#39;s gravatar image" />
<p><span>jusdespommes</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jusdespommes has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '20, 17:02</strong> </span></p>
</div>
</div>
<div id="comments-container-73245" class="comments-container">
&#10;</div>
<div id="comment-tools-73245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73245-form-container" class="comment-form-container">
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

<span id="73247"></span>

<div id="answer-container-73247" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73247-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-73247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>You just have to look also for relations.</p>
<p>Like this for example :</p>
<pre><code>[out:json];
nwr[&quot;natural&quot;~&quot;water&quot;] (around:5100.0, 51.508341, -0.125499); 
out meta;
&gt;; out skel qt;</code></pre>
<p>It much slower, but should be complete.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Feb '20, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73247" class="comments-container">
<span id="73296"></span>
<div id="comment-73296" class="comment">
<div id="post-73296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ahh, this is so good.</p>
<p>What's the 'nwr' doing in contrast to my original query?</p>
<p>Thank you so much!</p>
</div>
<div id="comment-73296-info" class="comment-info">
<span class="comment-age">(29 Feb '20, 19:33)</span> <span class="comment-user userinfo">jusdespommes</span>
</div>
</div>
<span id="73297"></span>
<div id="comment-73297" class="comment">
<div id="post-73297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>nwr combines the node way and rel keywords. So it also fetch the relations matching the keyword.</p>
</div>
<div id="comment-73297-info" class="comment-info">
<span class="comment-age">(29 Feb '20, 19:37)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73298"></span>
<div id="comment-73298" class="comment">
<div id="post-73298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can use the clause <code>relation["type"="multipolygon"]["natural"="water"]*</code> to query multipolygons specifically. (I will let someone else supplement on its performance). Don't forget nodes, as some water features may only be mapped in that format.</p>
</div>
<div id="comment-73298-info" class="comment-info">
<span class="comment-age">(01 Mar '20, 10:31)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-73247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73247-form-container" class="comment-form-container">
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

