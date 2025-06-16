+++
type = "question"
title = "Driving school area"
description = '''Hello. Are there any ways to correctly tag an area, where driving school instructors teach newbie drivers?  If I tag the whole area as amenity=driving_school then for some reason this whole territory disappears from the map, which we can see on openstreetmap.org. If I tag it as amenity=parking, then...'''
date = "2015-03-04T21:39:00Z"
lastmod = "2017-09-06T08:36:00Z"
weight = 41493
keywords = [ "driving", "tagging" ]
aliases = [ "/questions/41493" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Driving school area](/questions/41493/driving-school-area)

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
<span id="post-41493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41493-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. Are there any ways to correctly tag an area, where driving school instructors teach newbie drivers? If I tag the whole area as amenity=driving_school then for some reason this whole territory disappears from the map, which we can see on openstreetmap.org. If I tag it as amenity=parking, then the territory is showing up, but actually it is not a parking area, so the tagging will be incorrect.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-driving" rel="tag" title="see questions tagged &#39;driving&#39;">driving</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '15, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7beec6d85fed7bf5255d6657d7609ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sergey%20Karavay&#39;s gravatar image" />
<p><span>Sergey Karavay</span><br />
<span class="score" title="539 reputation points">539</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sergey Karavay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41493" class="comments-container">
<span id="41501"></span>
<div id="comment-41501" class="comment">
<div id="post-41501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am not sure about the location situation here. I guess it would look somehow like a parking space in reality?! I think we do not have such in Germany, at least not for most driving schools. Is it just a practical practise area and the main driving school (theory, office) is somewhere else in the city? Then this tagging can be hard to do. One driving school should not get two objects being tagged as <code>driving_school</code>. A possible way would be to map the school as a multipolygon with that tag.</p>
</div>
<div id="comment-41501-info" class="comment-info">
<span class="comment-age">(05 Mar '15, 00:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41493-form-container" class="comment-form-container">
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

<span id="41500"></span>

<div id="answer-container-41500" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41500-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sergey Karavay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tags you choose for any object should in most cases reflect the current method of tagging seen in the wiki and in <a href="http://taginfo.openstreetmap.org/search?q=amenity%3Ddriving_school">Taginfo</a>. The tag amenity=driving_school has been used about 10,000 times so it would appear to be the correct tagging. The reason "it disappears from the map" is because that tag is not being rendered at the present time. There's really not much you can do about that except to hope that it will be one day or work toward getting the powers that be to add rendering for driving schools.</p>
<p>While that is frustrating, because we all want to see what we add to OSM, you shouldn't resort to tagging something merely to make it show up on the map or your GPS. OSM calls that "mapping for the renderer" which is frowned upon for many reasons. You have already said that in a different way in your last statement:</p>
<p>" If I tag it as amenity=parking, then the territory is showing up, but actually it is not a parking area, so the tagging will be incorrect."</p>
<p>Cheers</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '15, 00:26</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '15, 00:27</strong> </span></p>
</div>
</div>
<div id="comments-container-41500" class="comments-container">
<span id="41528"></span>
<div id="comment-41528" class="comment">
<div id="post-41528-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not clear to me if the original question refers to the actual school facility, or a private area for learning to drive outside of regular traffic. Some aspects (e.g. the comparison with a parking area and the phrasing "this whole territory") make me assume that it might be the latter, in which case amenity=driving_school would actually not be the correct tag.</p>
</div>
<div id="comment-41528-info" class="comment-info">
<span class="comment-age">(06 Mar '15, 01:22)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="41529"></span>
<div id="comment-41529" class="comment">
<div id="post-41529-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14/tordanik">@Tordanik</a>: yes, I think that is the what I am commenting on in my comment below the question. It would be good if <a href="https://help.openstreetmap.org/users/10543/sergey-karavay">@Sergey</a> could clarify this.</p>
</div>
<div id="comment-41529-info" class="comment-info">
<span class="comment-age">(06 Mar '15, 01:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41531"></span>
<div id="comment-41531" class="comment">
<div id="post-41531-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suppose that is a possibility but then, as you correctly state aseerel, the tagging becomes difficult. Creating a relation is a big pain and it won't necessarily give him what he wants either, which is to see the area on a map.</p>
<p>Sergey? What say you?</p>
</div>
<div id="comment-41531-info" class="comment-info">
<span class="comment-age">(06 Mar '15, 08:15)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59357"></span>
<div id="comment-59357" class="comment">
<div id="post-59357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Strange, I dud not get any notifications about this comments. Driving schools (in Belarus for this case) have a special territory with different obstacles there to learn different driving techniques. It looks like a big territory covered with asphalt (almost like simple parking)</p>
</div>
<div id="comment-59357-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 08:36)</span> <span class="comment-user userinfo">Sergey Karavay</span>
</div>
</div>
</div>
<div id="comment-tools-41500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41500-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41497"></span>

<div id="answer-container-41497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41497-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag%3Aamenity%3Ddriving_school">amenity=driving_school</a> does appear to be the tag people are using for driving schools.</p>
<p>Don't worry about it not showing up on the main map. There are many other maps based on the OpenStreetMap data and some of them may show objects with this tag. The most important thing is to tag the object correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '15, 00:06</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-41497" class="comments-container">
<span id="41498"></span>
<div id="comment-41498" class="comment">
<div id="post-41498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>… and map styles change: it may <a href="http://stefanosabatini.eu/doesitrender/#amenity=driving_school">show up even on the standard OSM.org map</a> at some day.</p>
</div>
<div id="comment-41498-info" class="comment-info">
<span class="comment-age">(05 Mar '15, 00:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41497-form-container" class="comment-form-container">
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

