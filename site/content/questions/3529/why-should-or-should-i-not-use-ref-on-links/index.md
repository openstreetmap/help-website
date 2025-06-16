+++
type = "question"
title = "Why should or should I not use ref=* on links?"
description = '''Summary: Is there an agreed upon convention on tagging road links (such as freeway on-ramps)? The discussion of pros and cons of using ref=* on links follows. Detailed problem description I am not naturally inclined to tag road links (freeway on- and off-ramps specifically) with a ref=*, but some pe...'''
date = "2011-03-04T19:35:00Z"
lastmod = "2011-03-28T23:23:00Z"
weight = 3529
keywords = [ "skobbler", "ref", "links", "tagging", "shields" ]
aliases = [ "/questions/3529" ]
osqa_answers = 6
osqa_accepted = true
+++

<div class="headNormal">

# [Why should or should I not use ref=\* on links?](/questions/3529/why-should-or-should-i-not-use-ref-on-links)

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
<span id="post-3529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3529-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Summary</strong>: Is there an agreed upon convention on tagging road links (such as freeway on-ramps)? The discussion of pros and cons of using ref=* on links follows.</p>
<p><strong>Detailed problem description</strong></p>
<p>I am not naturally inclined to tag road links (freeway on- and off-ramps specifically) with a ref=*, but some people in my area have done it copiously and meticulously. So an on-ramp from a road name El Toro Road to a freeway designated CA-73 would be tagged</p>
<p>name=CA-73 South onramp<br />
ref=from El Toro Road</p>
<p>See it <a href="http://osm.org/go/TPVwMxDU">here</a></p>
<p>It looks good in Mapnik and works well in Potlatch if you have a mess of links in the case where several freeways meet (the above example is not one). However, some tile makers and routing apps (notably skobbler) use the value of ref to put a shield on roads. It works fine when ref=I-405 or even ref=CR S18, but it gets a bit ugly with the example above, when the app places the entire "from El Toro Road" in a shield floating in the middle of a map. It takes a while (even with OSM knowledge) to figure out where it's coming from. I can imagine how confusing it is to drivers.</p>
<p>I know we're not here to serve skobbler users, and I will be bringing this up with skobbler developers to see if they can be more discriminate in displaying shields derived from ref tags. But at the same time, I did see some of the more experienced OSM editors advise to not use ref=* on links. Why is that? Is that because most of the users of OSM data will tend to misinterpret this info as a highway designation/shield? Wiki does not state one way or the other.</p>
<p>Should I start clearing up this data in my area? That does not feel right. I would much rather all tile generators and all routing apps would read the OSM editors' minds and know when and when not to show this info as a shield.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-skobbler" rel="tag" title="see questions tagged &#39;skobbler&#39;">skobbler</span> <span class="post-tag tag-link-ref" rel="tag" title="see questions tagged &#39;ref&#39;">ref</span> <span class="post-tag tag-link-links" rel="tag" title="see questions tagged &#39;links&#39;">links</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-shields" rel="tag" title="see questions tagged &#39;shields&#39;">shields</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '11, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '11, 22:18</strong> </span></p>
</div>
</div>
<div id="comments-container-3529" class="comments-container">
<span id="3534"></span>
<div id="comment-3534" class="comment">
<div id="post-3534-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No matter what answer gets accepted, I strongly recommend sending a polite request to the folks who are torquing the tags and pointing them to this question...</p>
</div>
<div id="comment-3534-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 20:46)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3541"></span>
<div id="comment-3541" class="comment">
<div id="post-3541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Absolutely will do that. The person who added the tags has personally surveyed (i.e., drove, recorder tracks and took photos), mapped and tagged thousands of miles of roads in the US Southwest. Without him, the OSM for Southern California, Nevada and Arizona would look very different.</p>
</div>
<div id="comment-3541-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 22:06)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3529-form-container" class="comment-form-container">
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

6 Answers:

</div>

</div>

<span id="3533"></span>

<div id="answer-container-3533" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3533-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The refs used there on those ramps appear to be valid values for exit_to= tags (save where they're "from" someplace, those would need to be updated, and it would need to be on the junction node at the start of the link, not the link itself. See <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dmotorway_junction">tag:motorway_junction</a> for details.</p>
<p>Also, I see most of the names are obviously wrong; <a href="https://wiki.openstreetmap.org/wiki/Name#Name_is_the_name_only">name is the name only</a>. Many of the names shown should be <a href="https://wiki.openstreetmap.org/wiki/Description">description=*</a> instead.</p>
<p>I don't see a problem with fixing the tags, though it does appear there is useful information available; I would try to preserve the existing, incorrectly tagged data by moving it to more widely accepted tags. If that doesn't satisfy whatever renderer they're using at that point, well, <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">that's the renderer's problem</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '11, 09:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-3533" class="comments-container">
<span id="3540"></span>
<div id="comment-3540" class="comment">
<div id="post-3540-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Very helpful, thanks!</p>
</div>
<div id="comment-3540-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 22:02)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3554"></span>
<div id="comment-3554" class="comment">
<div id="post-3554-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Paul, in the example above, can you explain which names are wrong and why? I read the "name is the name only" writeup on wiki. name="CA-73 and CA-133 North onramp"seems perfectly reasonable to me.</p>
<p>As far as where to move the values form ref=* on motorway_links, you mention that it should be a tag like exit_to on a motorway_junction. But as you yourself point out these are not exits, these are "entrances". So what would be the tagging schema for a node on the surface road where an onramp originates? I don't think it's in the wiki.</p>
</div>
<div id="comment-3554-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 09:12)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3578"></span>
<div id="comment-3578" class="comment">
<div id="post-3578-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's not the actual name of the road, though. It's a description of a road that very likely has no name or the same name as the adjacent freeway. It's generally unnecessary to tag what it's an enterence to...</p>
</div>
<div id="comment-3578-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 17:56)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3533-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3531"></span>

<div id="answer-container-3531" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3531-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-3531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using "ref=from El Toro Road" sounds very cludgy and (if it's not written anywhere as a reference number for the road) just wrong.</p>
<p>It's not just Skobbler that uses both ref= and name=; my Garmin reads both out too, and I'm sure that others do as well. Presumably that's why people are doing it - so that the Satnav says "take the CA-73 South onramp from El Toro Road".</p>
<p>If there's any doubt I'd map what's on the ground wherever possible, but I'd be a little reticent about cleaning up anything that someone else has spent a lot of time entering (even if it's wrong). I'd certainly try to engage them in some sort of dialog to try and figure out what what they're doing, and also present the arguments in favour of recording what's on the ground rather than what works well in one particular application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 20:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-3531" class="comments-container">
<span id="3532"></span>
<div id="comment-3532" class="comment">
<div id="post-3532-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A very reasonable opinion that reflects mine. But it is still an opinion, isn't it? Opinions, someone will tell us shortly, belong in the forum. If there is a definitive answer, I am hoping to hear it soon.</p>
</div>
<div id="comment-3532-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 20:11)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3536"></span>
<div id="comment-3536" class="comment">
<div id="post-3536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does "Fake Steve C" add answers here? Perhaps he should - they'd certainly be "definitive". Not necessarily "reasonable", though.</p>
<p>Seriously though, it's very difficult to have definitive answers in a collaborative project. Everyone doing what they think is right is a good start, though.</p>
</div>
<div id="comment-3536-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 21:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-3531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3531-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3548"></span>

<div id="answer-container-3548" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3548-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi. I'm the guy doing the tagging in question.</p>
<p>First, I appreciate the way this is being discussed - it's my ideal of "the OSM way".</p>
<p>When I started tagging these, there was no agreed-upon method, so I tried to use existing tags in a way that was close to their purpose. It seemed particular useful for navigation to name the ramps as I did.</p>
<p>I didn't want to lose the information I put in ref yet because I wasn't sure exactly how it would/could be derived in the future. The ref tag was documented as a free-form place to put any sort of non-name reference information. Since then, certain patterns in that field have been defined and recognized to be shown as shields, but I believe skobbler is doing the wrong thing in this case, because "from El Toro Road" doesn't look like any of those defined patterns.</p>
<p>So, here's my current approach:</p>
<p>Exit node - node where exit ramp originates at motorway:</p>
<pre><code>&quot;highway&quot;=&quot;motorway_junction&quot;
&quot;is_in:state_code&quot;=&quot;CA&quot;     # Helps to backtrack exit # to correct state db
&quot;ref&quot;=&quot;54&quot;              # Exit #
&quot;name&quot;=&quot;Mountain Ave&quot;       # Name on sign
&quot;towards&quot;=&quot;Mt. Baldy&quot;       # Destination name on sign
&#10;&quot;milepost:state&quot;=*          # To be imported from state db
&quot;milepost:county&quot;=*         # To be imported from state db
&quot;is_in:county&quot;=*            # To be imported from state db
&quot;is_in:city&quot;=*          # To be imported from state db</code></pre>
<p>Exit ramp - motorway_link from motorway to street:</p>
<pre><code>&quot;highway&quot;=&quot;motorway_link&quot;
&quot;ref&quot;=&quot;Exit 54 from CA-210 East&quot;
&quot;name&quot;=&quot;Mountain Ave offramp&quot;
&quot;towards&quot;=&quot;Mt. Baldy&quot;</code></pre>
<p>Entrance ramp - motorway_link from street/motorway to motorway:</p>
<pre><code>&quot;highway&quot;=&quot;motorway_link&quot;
&quot;ref&quot;=&quot;Exit 64A from CA-210 East&quot;
&quot;name&quot;=&quot;I-15 South onramp&quot;
&quot;towards&quot;=&quot;San Diego&quot;</code></pre>
<p>I believe I recognized that the "name" tag would be most likely to be immediately used by nav and rendering, and so put what seemed correct for them there and stuck the rest of the description in ref. I'd not be averse to separating those back out of ref into their own tags if you can suggest them. I'm not convinced they are ready to be dropped completely, and I don't think there's compelling space/size argument to be made.</p>
<p>Anyway, just out the door for the weekend - I'll be back to discuss/resolve next week.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/21442ab2e91c182468beeb96d02a09be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AM909&#39;s gravatar image" />
<p><span>AM909</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AM909 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3548" class="comments-container">
<span id="3556"></span>
<div id="comment-3556" class="comment">
<div id="post-3556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think the current ref=* values should be dropped completely, but I think they should be moved to an innocuous tag, such as description=* or even note=*</p>
<p>By the same token, I don't see a problem with your values for name=* for these onramps, the way Paul above does. I would not touch those. I just want to clear up the shields from the skobbler maps and who knows what other mapping/routing apps.</p>
<p>I did write to skobbler to tell them they should either be smarter about contents of shields or drop shields from motorway_links altogether.</p>
</div>
<div id="comment-3556-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 09:15)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3576"></span>
<div id="comment-3576" class="comment">
<div id="post-3576-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm just agreeing with the established, well-documented practice on the name tag: Name should be the name, putting a description in the name is just tagging wrong for a specific renderer...</p>
</div>
<div id="comment-3576-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 16:15)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3721"></span>
<div id="comment-3721" class="comment">
<div id="post-3721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I disagree that it is not the name of the road. If the public works department creates a work ticket for these ramps or connectors, it is very likely to name it almost exactly name+ref (well, at least the "from..." part of ref). The line between name and description is often blurred with frontage roads, service roads, etc. Because description is specifically defined as non-rendering, I lean toward using name because I think the information is useful to render, particularly for routers.</p>
</div>
<div id="comment-3721-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 13:47)</span> <span class="comment-user userinfo">AM909</span>
</div>
</div>
</div>
<div id="comment-tools-3548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3548-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3723"></span>

<div id="answer-container-3723" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3723-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry for the delay.</p>
<p>So, how about:</p>
<p>For an offramp, or connector between trunks or higher:<br />
<code>"ref" = "Exit 54 from CA-210 East"</code><br />
<code>"name" = "Mountain Ave offramp"</code><br />
</p>
<p>remove ref tag and add:<br />
<code>"exit_ref" = "54"</code><br />
<code>"exit_from" = "CA-210"</code><br />
<code>"exit_from_dir" = "East"</code><br />
</p>
<p>for an onramp:<br />
<code>"ref" = "from Foothill Blvd North"</code><br />
<code>"name" = "I-210 East onramp"</code><br />
</p>
<p>remove ref tag and add:<br />
<code>"entrance_from" = "Foothill Blvd"</code><br />
<code>"entrance_from_dir" = "North"</code><br />
</p>
<p>Assuming this is OK, how long should I wait for comment before doing this? Should I mention it on the tagging or talk-us list? I intend to download all the ramps I've tagged using XAPI, fix the tags with a perl script, inspect in JOSM, and upload the changes. Should take less than an hour and hopefully not result in any conflicts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '11, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/21442ab2e91c182468beeb96d02a09be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AM909&#39;s gravatar image" />
<p><span>AM909</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AM909 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '11, 14:17</strong> </span></p>
</div>
</div>
<div id="comments-container-3723" class="comments-container">
<span id="3734"></span>
<div id="comment-3734" class="comment">
<div id="post-3734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still not quite there. How about this: On the node where the motorway and motorway_link meet for the exit, "ref = 54" and "name = Mountain Avenue". On the exit ramp itself, no ref, no name (unless it's a case where a state highway uses that ramp to leave a motorway and go to another way, then the highway's name and ref would be appropriate. Not sure "[enterance|exit]_from" are widely used, and seeing them rendered or used by anything is unlikely as a result. (more in next comment).</p>
</div>
<div id="comment-3734-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 18:29)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3735"></span>
<div id="comment-3735" class="comment">
<div id="post-3735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Name should just be the name, ref should just be the reference. For your onramp example, I wouldn't use either tag (except in the same highway-takes-the-ramp example above). "description = I 210 East onramp from Foothill Boulevard North" would be more appropriate. There's nothing stopping you from using exit_from or entrance_from tags, but again, not sure what their use would be.</p>
</div>
<div id="comment-3735-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 18:31)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3736"></span>
<div id="comment-3736" class="comment">
<div id="post-3736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the goal is to show how one gets to or from a particular motorway route to surface streets, this is probably better handled by adding the motorway_links as "link" members of the relation for the route on the motorway.</p>
</div>
<div id="comment-3736-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 18:32)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3837"></span>
<div id="comment-3837" class="comment">
<div id="post-3837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I hope we get a resolution soon. Alan, I would run this through the tagging list and see if there is consensus or at least enough encouragement to go with some version of your schema. That said, should you simply change all ref=* on motorway_links to description=* the way Paul seems to be suggesting, I will not object. It seems our main concern is preserving the data no matter how superfluous it appears to be at the moment, while cleaning up the rendered driving maps (e.g., skobbler, but probably others as well)</p>
</div>
<div id="comment-3837-info" class="comment-info">
<span class="comment-age">(16 Mar '11, 05:02)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-3723" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3723-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4156"></span>

<div id="answer-container-4156" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4156-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-4156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do want to retain the information for reasons I've described earlier.</p>
<p>On talk-us, Mike N is proposing that <code>name=*</code> be changed to <code>exit_to=*</code> for all but "named exits" - I'm waiting for clarification on what that means. Does <code>exit_to=*</code> render like <code>name=*</code>, or will this result in the exit names disappearing from the map, and is that desirable?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '11, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/21442ab2e91c182468beeb96d02a09be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AM909&#39;s gravatar image" />
<p><span>AM909</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AM909 has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '11, 16:45</strong> </span></p>
</div>
</div>
<div id="comments-container-4156" class="comments-container">
<span id="4157"></span>
<div id="comment-4157" class="comment">
<div id="post-4157-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>It depends on the renderer. Don't incorrectly tag for any particular renderer.</p>
</div>
<div id="comment-4157-info" class="comment-info">
<span class="comment-age">(28 Mar '11, 16:45)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-4156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4156-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4158"></span>

<div id="answer-container-4158" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4158-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-4158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In this case, which came first, the renderer or the database? Both MapNik and OsmaRender show the exit names, presumably intentionally. Shouldn't any change in that particular functionality be co-ordinated with the renderer developers, and discussed by more than 3 of us?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '11, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/21442ab2e91c182468beeb96d02a09be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AM909&#39;s gravatar image" />
<p><span>AM909</span><br />
<span class="score" title="29 reputation points">29</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AM909 has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-4158" class="comments-container">
<span id="4159"></span>
<div id="comment-4159" class="comment">
<div id="post-4159-score" class="comment-score">
3
</div>
<div class="comment-text">
<ol>
<li><p>Use comments for comments, not new answers.</p></li>
<li><p>There's more renderers than just Mapnik and Osmarender. Mkgmap and various other navigation software, for example.</p></li>
</ol>
</div>
<div id="comment-4159-info" class="comment-info">
<span class="comment-age">(28 Mar '11, 16:51)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="4164"></span>
<div id="comment-4164" class="comment">
<div id="post-4164-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, there is also more languages than English. Think about that OSM maps get rendered in many different languages. How would a software know that "offramp" is a description that should be translated, and Mountain Ave is a name that should not be translated?</p>
</div>
<div id="comment-4164-info" class="comment-info">
<span class="comment-age">(28 Mar '11, 23:23)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-4158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4158-form-container" class="comment-form-container">
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

