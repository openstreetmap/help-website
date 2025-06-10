+++
type = "question"
title = "Overpass QL: get entire street (way) of location."
description = '''Hi, With the help of this forum I found a way to retrieve the street that belongs to a specific lat/lon. I use the following code: &amp;lt;osm-script output=&quot;json&quot;&amp;gt;  &amp;lt;query type=&quot;way&quot;&amp;gt;  &amp;lt;around lat=&quot;52.15809830545579&quot; lon=&quot;6.402184798522356&quot; radius=&quot;10&quot;/&amp;gt;  &amp;lt;has-kv k=&quot;highway&quot; modv=&quot;&quot; v...'''
date = "2021-11-03T22:38:00Z"
lastmod = "2022-02-09T12:48:00Z"
weight = 82469
keywords = [ "ways", "streetcomplete", "overpass-ql" ]
aliases = [ "/questions/82469" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass QL: get entire street (way) of location.](/questions/82469/overpass-ql-get-entire-street-way-of-location)

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
<span id="post-82469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82469-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>With the help of this forum I found a way to retrieve the street that belongs to a specific lat/lon. I use the following code:</p>
<pre><code>&lt;osm-script output=&quot;json&quot;&gt;
  &lt;query type=&quot;way&quot;&gt;
    &lt;around lat=&quot;52.15809830545579&quot; lon=&quot;6.402184798522356&quot; radius=&quot;10&quot;/&gt;
    &lt;has-kv k=&quot;highway&quot; modv=&quot;&quot; v=&quot;&quot;/&gt;
  &lt;/query&gt;
  &lt;union&gt;
    &lt;item/&gt;
    &lt;recurse type=&quot;down&quot;/&gt;
  &lt;/union&gt;
  &lt;print/&gt;
&lt;/osm-script&gt;</code></pre>
<p><a href="http://overpass-turbo.eu/s/1cGM">This Overpass query</a> has got two downfalls. Not always the entire street is shown, enlarging the raduis will select more of the current street, but also results in other streets in the dataset.</p>
<p>What do I need to change to always get one entire street (way), even if the way is for example 1000 km long?</p>
<p>Anyone an idea?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-streetcomplete" rel="tag" title="see questions tagged &#39;streetcomplete&#39;">streetcomplete</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Nov '21, 22:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f972fd93a4401edb23b6ee0bc6136ba2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arjan&#39;s gravatar image" />
<p><span>Arjan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arjan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82469" class="comments-container">
<span id="83422"></span>
<div id="comment-83422" class="comment">
<div id="post-83422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like I found a solution, but I don't get it to work? <a href="https://github.com/drolbr/Overpass-API/issues/95#issuecomment-291252449">https://github.com/drolbr/Overpass-API/issues/95#issuecomment-291252449</a></p>
</div>
<div id="comment-83422-info" class="comment-info">
<span class="comment-age">(09 Feb '22, 12:48)</span> <span class="comment-user userinfo">Arjan</span>
</div>
</div>
</div>
<div id="comment-tools-82469" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82469-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

