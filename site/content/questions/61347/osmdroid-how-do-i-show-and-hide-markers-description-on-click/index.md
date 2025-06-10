+++
type = "question"
title = "Osmdroid: how do i show and hide markers description on click?"
description = '''I am programming an app in Java using Android Studio. I already displayed a map using osmdroid, added some overlays to display markers on special locations and added a title &amp;amp; a description to the markers. Now I display the title &amp;amp; description of the marker on click using the setFocusItemsOn...'''
date = "2017-12-24T13:20:00Z"
lastmod = "2017-12-24T13:20:00Z"
weight = 61347
keywords = [ "osmdroid", "java", "focus", "overlay" ]
aliases = [ "/questions/61347" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Osmdroid: how do i show and hide markers description on click?](/questions/61347/osmdroid-how-do-i-show-and-hide-markers-description-on-click)

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
<span id="post-61347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61347-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am programming an app in Java using Android Studio. I already displayed a map using osmdroid, added some overlays to display markers on special locations and added a title &amp; a description to the markers.</p>
<p>Now I display the title &amp; description of the marker on click using the setFocusItemsOnTap method. My problem is that I am not able to hide the title &amp; description of the marker on a second click (so if its already shown). Is there any way to do this?</p>
<p>Or if thats not possible is there a way to only display the title &amp; description of one marker at once using the setFocusItemsOnTab methode?</p>
<pre><code>public static List&lt;OverlayItem&gt; items = new ArrayList&lt;OverlayItem&gt;();
//[...]
items.add(new OverlayItem(&quot;uid1&quot;,&quot;Title&quot;, &quot;Description&quot;, new GeoPoint(51.398,6.875)));
//[...]
List&lt;OverlayItem&gt; currentList;
currentList = new ArrayList&lt;OverlayItem&gt;();
    currentList.add(items.get(i));
//[...]
final ItemizedOverlayWithFocus&lt;OverlayItem&gt; mOverlay = new ItemizedOverlayWithFocus&lt;OverlayItem&gt;(this, currentList, new ItemizedIconOverlay.OnItemGestureListener&lt;OverlayItem&gt;() {
            @Override
            public boolean onItemSingleTapUp(final int index, final OverlayItem item) {
                //here it should decide if the title &amp; description is already shown or not. (true =&gt; hide it, false =&gt; display it)
                return true;
            }
            @Override
            public boolean onItemLongPress(final int index, final OverlayItem item) {
                return false;
            }
    });
mOverlay.setFocusItemsOnTap(true);</code></pre>
<p>I have to use these parts of the code, because i wanted to add different markers and i wanted to be able to focus all of them. Also i need to be able to add them to a dynamic list during runtime.</p>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-focus" rel="tag" title="see questions tagged &#39;focus&#39;">focus</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Dec '17, 13:20</strong></p>
<img src="https://secure.gravatar.com/avatar/b2ae55cba5ad60a0e937eb7b42c7a99c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve1242&#39;s gravatar image" />
<p><span>steve1242</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve1242 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61347" class="comments-container">
&#10;</div>
<div id="comment-tools-61347" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61347-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

