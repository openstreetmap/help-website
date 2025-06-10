+++
type = "question"
title = "How To Correct Waterways Intersecting Roads Without A Junction Node?"
description = '''I&#x27;m looking at http://keepright.ipax.at and trying to correct some of the problems in my area. The majority seem to be &quot;This highway intersects the waterway but there is no junction node&quot;. This seems to me to be correct as, unless the waterway routinely flows across the road (a ford!) there is no ju...'''
date = "2011-02-15T02:01:00Z"
lastmod = "2013-09-20T04:44:00Z"
weight = 3049
keywords = [ "waterway", "tag", "keepright", "highway", "intersection" ]
aliases = [ "/questions/3049" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How To Correct Waterways Intersecting Roads Without A Junction Node?](/questions/3049/how-to-correct-waterways-intersecting-roads-without-a-junction-node)

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
<span id="post-3049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3049-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-3049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking at <a href="http://keepright.ipax.at">http://keepright.ipax.at</a> and trying to correct some of the problems in my area. The majority seem to be "This highway intersects the waterway but there is no junction node". This seems to me to be correct as, unless the waterway routinely flows across the road (a ford!) there is no junction. The renderer seems to draw the road over the waterway in the ones I've looked at so far.</p>
<p>How do you think I should I fix this?<br />
a) Tell keepright that it's a false positive and to ignore it?<br />
b) Give the waterway a layer of -1?<br />
c) Add a junction node but mark it as tunnel=culvert layer=-1 However in some cases I imagine that there is probably a bridge but the mapper has failed to note this in OSM so this is not the most viable/accurate option.<br />
d) Go and check each one out individually, and then...?</p>
<p>I favour option b.</p>
<p>What say you?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-keepright" rel="tag" title="see questions tagged &#39;keepright&#39;">keepright</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '11, 02:01</strong></p>
<img src="https://secure.gravatar.com/avatar/956d6fda0f51e8001832540fa2c716a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vagabond&#39;s gravatar image" />
<p><span>vagabond</span><br />
<span class="score" title="195 reputation points">195</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vagabond has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-3049" class="comments-container">
<span id="3129"></span>
<div id="comment-3129" class="comment">
<div id="post-3129-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would avoid setting layer tags unless you have multiple bridges, or multiple tunnels crossing. Otherwise, let the renderers sort it out, they're pretty good about being able to tell that a tunnel is below the surface, the surface is the surface, and bridges are above the surface. You only really need "layer" tags when you have situations like double-decker bridges on a divided highway, motorway interchanges, major subway stations, and the like, where multiple of the same kind of thing (multiple bridges, multiple tunnels) cross each other.</p>
</div>
<div id="comment-3129-info" class="comment-info">
<span class="comment-age">(17 Feb '11, 06:12)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3049" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3049-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="3050"></span>

<div id="answer-container-3050" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3050-score" class="post-score" title="current number of votes">
15
</div>
<span id="post-3050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why mark it as a false positive when it isn't?</p>
<p>Tunnels should not be marked as a junction nodes, but as ways. See: <a href="http://wiki.openstreetmap.org/wiki/Tunnel">Key:tunnel</a></p>
<p>I would suggest d). If the waterway flows in a culvert then enter it as a culvert. If the way runs over a bridge, then enter it as a bridge. If it's a ford, then enter it as a ford. If it's an aqueduct, then enter it as an aqueduct, etc, etc..</p>
<p>I advice against filling the OSM database with guesses just to make our debugging tools happy. The tools are there to help us find issues where we may need to collect more fact.</p>
<p>By the way I'm more worried about how the routing softwares handle those issues, than the prevalence of a minor artefact in a rendered map intended for the human eye. A strict routing software might refuse to route your wheelchair via the faintly defined crossing with the river.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '11, 02:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '11, 02:53</strong> </span></p>
</div>
</div>
<div id="comments-container-3050" class="comments-container">
<span id="3084"></span>
<div id="comment-3084" class="comment">
<div id="post-3084-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Definitely "d". If you've not been to the location, you don't know what's there, do you?</p>
</div>
<div id="comment-3084-info" class="comment-info">
<span class="comment-age">(15 Feb '11, 19:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="3111"></span>
<div id="comment-3111" class="comment">
<div id="post-3111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If the waterway and the highway don't actually cross (due to one being on a bridge or the other in a culvert), is an intersection node actually necessary? My understanding is that such a waterway-highway joined node would be indicative of a ford or a boat ramp, where one could potentially turn off the highway and use the waterway as a route if they were operating an amphibious vehicle or not adverse to swimming...</p>
</div>
<div id="comment-3111-info" class="comment-info">
<span class="comment-age">(16 Feb '11, 17:06)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3122"></span>
<div id="comment-3122" class="comment">
<div id="post-3122-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ways crossing on different layers should not have a common junction node. Otherwise KeepRight will write messages like "This node is a junction of ways on different layers" and "Connected ways should be on the same layer. Crossings on intermediate nodes of ways on different layers are obviously wrong. Junctions on end-nodes of ways on different layers are also deprecated, but common practice. So you may ignore this part of the check and switch them off separately. Please note that bridges are set to layer +1, and tunnels to -1, anything else to layer 0 implicitly if no layer tag is present."</p>
</div>
<div id="comment-3122-info" class="comment-info">
<span class="comment-age">(16 Feb '11, 20:03)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="3136"></span>
<div id="comment-3136" class="comment">
<div id="post-3136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I've found setting the layer tag for those three levels generally does more harm than good in most cases.</p>
</div>
<div id="comment-3136-info" class="comment-info">
<span class="comment-age">(17 Feb '11, 19:08)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3050-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3131"></span>

<div id="answer-container-3131" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3131-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Go and survey the place and map what is actually there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '11, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-3131" class="comments-container">
&#10;</div>
<div id="comment-tools-3131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3131-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3051"></span>

<div id="answer-container-3051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3051-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would recommend option C or D:</p>
<ul>
<li>a: is not technically a false positive</li>
<li>b: In the past there have been those who go through and made mass "corrections" to waterways having just a layer of -1, on the basis that it's a "Ground level feature". (Which I disagree with)</li>
<li>c: You are correct - most are culverts, but many will be bridges</li>
<li>d: Just leave them since there is no immediate harm to routing, etc; correct them as they are surveyed.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '11, 02:56</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '11, 02:57</strong> </span></p>
</div>
</div>
<div id="comments-container-3051" class="comments-container">
<span id="3110"></span>
<div id="comment-3110" class="comment">
<div id="post-3110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Some of the ways I've been mapping are tracks and trails across moors and many of these will indeed be fords and therefore pukka intersections.</p>
<p>Many thanks for the responses.</p>
</div>
<div id="comment-3110-info" class="comment-info">
<span class="comment-age">(16 Feb '11, 17:00)</span> <span class="comment-user userinfo">vagabond</span>
</div>
</div>
</div>
<div id="comment-tools-3051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3051-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7324"></span>

<div id="answer-container-7324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7324-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree with Paul Johnson, the only nodes where roads/rail should intersect water would be fords (or boat ramps), everything else they should be unattached</p>
<p>There is of course the odd time where the river (canal, ditch) is actually on a bridge.</p>
<p>Of course there is also THIS... canal crosses a river, and Interstate 10 crosses both. Of course it doesn't render accurately. <a href="http://www.openstreetmap.org/?lat=30.04535&amp;lon=-94.149314&amp;zoom=18&amp;layers=M">http://www.openstreetmap.org/?lat=30.04535&amp;lon=-94.149314&amp;zoom=18&amp;layers=M</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 23:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f6827fbcbfc77428dfb7f8743ab775db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sundance&#39;s gravatar image" />
<p><span>Sundance</span><br />
<span class="score" title="467 reputation points">467</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sundance has one accepted answer">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '11, 23:48</strong> </span></p>
</div>
</div>
<div id="comments-container-7324" class="comments-container">
<span id="7328"></span>
<div id="comment-7328" class="comment">
<div id="post-7328-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are not entirely right. Osmarender renders it correctly (the bridges).<br />
More importantly it does not seem to be mapped right. The river with riverbanks should have a single way for the flow inside (one that corresponds to the river network topology. And the same goes for the canal. It should be drawn as one waterway=canal only, perhaps bound in natural=water area. If you go east along the canal you get to pipes that are likely used to transfer the canal water over the river, but is not mapped at all and the second river/canal is also not...<br />
+1 for the nice example</p>
</div>
<div id="comment-7328-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 00:13)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-7324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7324-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7320"></span>

<div id="answer-container-7320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7320-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I recommend not taking KeepRight too seriously here. Just turn off the <em>waterway/highway</em> checkbox and be happy:</p>
<ul>
<li>The rendering tools do a fine job of drawing this case.</li>
<li>The routing tools are not confused either way.</li>
<li>The solutions are often worse than the problem.</li>
</ul>
<p>If you feel compelled to act, and you know which streams cross at the same level as the road, you can create a junction node and tag it: <a href="http://wiki.openstreetmap.org/wiki/Key:ford">http://wiki.openstreetmap.org/wiki/Key:ford</a>. In times of high water knowing which road crossings are definitely wet can be helpful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/372fabe5d3962d54b0c9474e35a05359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bryce%20C%20Nesbitt&#39;s gravatar image" />
<p><span>Bryce C Nesbitt</span><br />
<span class="score" title="345 reputation points">345</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bryce C Nesbitt has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-7320" class="comments-container">
<span id="26521"></span>
<div id="comment-26521" class="comment">
<div id="post-26521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To bad you can't turn off the waterway/highway checking in JOSM. The error messages complaining about crossing ways when there is a way on a bridge over a river are a constant frustration to this user.</p>
</div>
<div id="comment-26521-info" class="comment-info">
<span class="comment-age">(20 Sep '13, 04:44)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-7320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7320-form-container" class="comment-form-container">
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

