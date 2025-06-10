+++
type = "question"
title = "ItemizedOverlayWithBubble on top of the marker"
description = '''I want to put my ItemizedOverlayWithBubble by OSMdroid on top of the marker, because now it&#x27;s on the marker and when it shows my marker hides behind the bubble, because it&#x27;s the same GeoPoint. What is the correct way?  final ArrayList&amp;lt;ExtendedOverlayItem&amp;gt; items = new ArrayList&amp;lt;ExtendedOverl...'''
date = "2014-01-12T16:39:00Z"
lastmod = "2014-01-12T22:42:00Z"
weight = 29767
keywords = [ "marker", "osmdroid", "overlay" ]
aliases = [ "/questions/29767" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ItemizedOverlayWithBubble on top of the marker](/questions/29767/itemizedoverlaywithbubble-on-top-of-the-marker)

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
<span id="post-29767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29767-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to put my ItemizedOverlayWithBubble by OSMdroid on top of the marker, because now it's on the marker and when it shows my marker hides behind the bubble, because it's the same GeoPoint. What is the correct way?</p>
<pre><code>    final ArrayList&lt;ExtendedOverlayItem&gt; items = new ArrayList&lt;ExtendedOverlayItem&gt;();
    ExtendedOverlayItem a = new ExtendedOverlayItem(&quot;Hannover&quot;, &quot;SampleDescription&quot;, new GeoPoint(42.34105549, -3.69639444), this);
    items.add(0, a);
    ItemizedOverlayWithBubble&lt;ExtendedOverlayItem&gt; mMyLocationOverlay = 
            new ItemizedOverlayWithBubble&lt;ExtendedOverlayItem&gt;
            (this, items, mapView);
    mapView.getOverlays().add(mMyLocationOverlay);</code></pre>
<p>Thanks a lot</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '14, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/9ea3de739d59b5b6815a751ac302acdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marioerro&#39;s gravatar image" />
<p><span>marioerro</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marioerro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '14, 00:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-29767" class="comments-container">
<span id="29773"></span>
<div id="comment-29773" class="comment">
<div id="post-29773-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you have a look at the #osmdroid questions, you will recognize that they aren't answered that often. So you might use the official OSMdroid support channels instead to get a quick answer :/</p>
</div>
<div id="comment-29773-info" class="comment-info">
<span class="comment-age">(12 Jan '14, 18:22)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-29767" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29767-form-container" class="comment-form-container">
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

<span id="29781"></span>

<div id="answer-container-29781" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29781-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<pre><code>a.setMarkerHotspot(OverlayItem.HotspotPlace.TOP_CENTER);</code></pre>
<p>If someone want to know the solution, this is the solution</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '14, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/9ea3de739d59b5b6815a751ac302acdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marioerro&#39;s gravatar image" />
<p><span>marioerro</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marioerro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29781" class="comments-container">
&#10;</div>
<div id="comment-tools-29781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29781-form-container" class="comment-form-container">
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

