+++
type = "question"
title = "write an osm file to a different path"
description = '''Hi im trying to filter an osm file but i want the created file, to be in different folder rather than one im currently in, the command i use is  sudo osmosis --read-pbf &quot;/home/ubuntu/osmosis/bin/andorra-latest.osm.pbf&quot; --tf accept-ways highway=motorway,motorway_link,trunk,trunk_link --tf reject-rela...'''
date = "2020-11-26T17:42:00Z"
lastmod = "2020-11-26T18:05:00Z"
weight = 77737
keywords = [ "filter", "osm", "osmosis" ]
aliases = [ "/questions/77737" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [write an osm file to a different path](/questions/77737/write-an-osm-file-to-a-different-path)

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
<span id="post-77737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77737-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi im trying to filter an osm file but i want the created file, to be in different folder rather than one im currently in, the command i use is sudo osmosis --read-pbf "/home/ubuntu/osmosis/bin/andorra-latest.osm.pbf" --tf accept-ways highway=motorway,motorway_link,trunk,trunk_link --tf reject-relation --used-node --write-xml "home/ubuntu/osmosis/bin/andorra-latest.osm"</p>
<p>this is the path i want to write my xml to --write-xml "home/ubuntu/osmosis/bin/andorra-latest.osm"</p>
<p>this is the error i am getting :</p>
<p>Caused by: java.io.FileNotFoundException: home/ubuntu/osmosis/bin/andorra-latest.osm (No such file or directory) any help would be much appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '20, 17:42</strong></p>
<img src="https://secure.gravatar.com/avatar/87f23f2f0056b2d7d6ed1760463ea1c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shafi-as&#39;s gravatar image" />
<p><span>shafi-as</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shafi-as has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77737" class="comments-container">
&#10;</div>
<div id="comment-tools-77737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77737-form-container" class="comment-form-container">
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

<span id="77739"></span>

<div id="answer-container-77739" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77739-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are missing a / before the "home" in your output path:</p>
<pre><code>/home/ubuntu/osmosis/bin/andorra-latest.osm</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '20, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '20, 17:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-77739" class="comments-container">
<span id="77740"></span>
<div id="comment-77740" class="comment">
<div id="post-77740-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks appreciate it :)</p>
</div>
<div id="comment-77740-info" class="comment-info">
<span class="comment-age">(26 Nov '20, 18:05)</span> <span class="comment-user userinfo">shafi-as</span>
</div>
</div>
</div>
<div id="comment-tools-77739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77739-form-container" class="comment-form-container">
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

