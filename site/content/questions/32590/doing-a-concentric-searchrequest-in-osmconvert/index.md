+++
type = "question"
title = "doing a concentric searchrequest in osmconvert"
description = '''i e round hamburg or paris to perform a search request - let me say in the concentric area of 50 km round hamburg or - let me say paris....  /tmp$ osmconvert oberbayern-latest.osm.pbf --all-to-nodes -o=blablubbla_2.o5m /tmp$ osmfilter blablubbla_2.o5m --keep=&quot;amenity=restaurant&quot; -o=my_gooddata_.o5m ...'''
date = "2014-04-23T22:29:00Z"
lastmod = "2014-04-23T22:44:00Z"
weight = 32590
keywords = [ "openstreetmap", "osmconvert" ]
aliases = [ "/questions/32590" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [doing a concentric searchrequest in osmconvert](/questions/32590/doing-a-concentric-searchrequest-in-osmconvert)

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
<span id="post-32590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32590-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i e round hamburg or paris to perform a search request - let me say in the concentric area of 50 km round hamburg or - let me say paris....</p>
<pre><code>/tmp$ osmconvert oberbayern-latest.osm.pbf --all-to-nodes -o=blablubbla_2.o5m
/tmp$ osmfilter blablubbla_2.o5m --keep=&quot;amenity=restaurant&quot; -o=my_gooddata_.o5m
/tmp$ osmconvert my_gooddata_.o5m --csv=&quot;@id @lon @lat shop name addr:street addr:housenumber addr:city website email&quot; --csv-headline | more
@id     @lon    @lat    shop    name    addr:street     addr:housenumber        addr:city       website email
29950894        11.7415509      48.3978074              Parkcafe        Am Wörth        23      Freising        http://www.parkcafe-freising.de
32559987        11.7841034      47.8785126              Waldrestaurant Maxlmühle        Maxlmühle       2       Valley  http://www.maxlmuehle.de/
33047448        11.1863664      47.9072486              Hirschberg-Alm
34034075        11.6704030      48.1169551              Zum Goldenen Stern      Gartenstadtstraße       6       München
34072038        11.6707224      48.1093154              Franziskaner Garten     Friedenspromenade       45      München http://www.franziskanergarten.de/[/code]</code></pre>
<p>ia this doable with Osmconvert and filter?</p>
<p>look forward to hear from you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Apr '14, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32590" class="comments-container">
<span id="32591"></span>
<div id="comment-32591" class="comment">
<div id="post-32591-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Osmconvert supports polygons as boundary. Maybe you could use them.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Osmconvert#Clipping_based_on_a_Polygon">http://wiki.openstreetmap.org/wiki/Osmconvert#Clipping_based_on_a_Polygon</a></p>
<p>BTW: you've posted the exact same question on the German forum just a few minutes ago. For the future please decide which channel you want to use for your questions. Crossposting is not really nice.</p>
<p><a href="http://forum.openstreetmap.org/viewtopic.php?pid=415273#p415273">http://forum.openstreetmap.org/viewtopic.php?pid=415273#p415273</a></p>
</div>
<div id="comment-32591-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 22:44)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-32590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32590-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

