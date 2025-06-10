+++
type = "question"
title = "How to filter tags"
description = '''Hi,  I want to filtering tags (name) but only for a type of object. Indeed, I want to remove name for only amenity and building object. I tried but for the moment I don&#x27;t find the solution.  My last try was : osmfilter output2.osm --drop-tags=&quot;amenity=name&quot;&amp;gt; output1.osm  And I don&#x27;t know if it&#x27;s ...'''
date = "2015-03-20T14:50:00Z"
lastmod = "2015-03-22T13:41:00Z"
weight = 41823
keywords = [ "filter", "filtering", "tag", "osmfilter" ]
aliases = [ "/questions/41823" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter tags](/questions/41823/how-to-filter-tags)

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
<span id="post-41823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41823-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to filtering tags (name) but only for a type of object.</p>
<p>Indeed, I want to remove name for only amenity and building object. I tried but for the moment I don't find the solution. My last try was :</p>
<pre><code>osmfilter output2.osm --drop-tags=&quot;amenity=name&quot;&gt; output1.osm</code></pre>
<p>And I don't know if it's possible.</p>
<p>Thank you for your help.</p>
<p>Michael</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '15, 14:50</strong></p>
<img src="https://secure.gravatar.com/avatar/bdffbed318d44cf586ab141e1cf03611?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mickmac&#39;s gravatar image" />
<p><span>mickmac</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mickmac has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '15, 13:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-41823" class="comments-container">
&#10;</div>
<div id="comment-tools-41823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41823-form-container" class="comment-form-container">
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

<span id="41847"></span>

<div id="answer-container-41847" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41847-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your statement drops only object tags with the real value 'name' which isn't that you want to archive. So if you take a <a href="https://wiki.openstreetmap.org/wiki/Osmfilter#Drop_specific_Tags">look at the docs</a>, you see that you need a wildcard or at least open filter experession:</p>
<pre><code>./osmfilter a.o5m --drop-tags=&quot;oneway= name=&quot; -o=plain_ways.o5m</code></pre>
<p>You can also add an --keep="amenity=" to return only amenity nodes/ways/relations and remove their names (if this makes sense to your scenario?)</p>
<p>Edit: I changed the doc link to drop "Tags" as that is what is wanted here I think.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '15, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Nov '18, 22:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-41847" class="comments-container">
&#10;</div>
<div id="comment-tools-41847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41847-form-container" class="comment-form-container">
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

