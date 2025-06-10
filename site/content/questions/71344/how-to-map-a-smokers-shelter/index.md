+++
type = "question"
title = "How to map a Smoker&#x27;s Shelter?"
description = '''Recently, a local hospital changed their attitude to smoking. The entire premises is now a non-smoking area, with the exception of smoking pavilions, aka. smoker&#x27;s shelter, and a bunch of other designations. They look like these: (image on Wikipedia) (I won&#x27;t link embed the image directly) Basically...'''
date = "2019-10-28T12:17:00Z"
lastmod = "2019-11-02T19:28:00Z"
weight = 71344
keywords = [ "shelter", "building", "amenity", "tagging" ]
aliases = [ "/questions/71344" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to map a Smoker's Shelter?](/questions/71344/how-to-map-a-smokers-shelter)

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
<span id="post-71344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71344-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently, a local hospital changed their attitude to smoking. The entire premises is now a non-smoking area, with the exception of smoking pavilions, aka. smoker's shelter, and a bunch of other designations.</p>
<p>They look like these: <a href="https://en.wikipedia.org/wiki/File:Smoking_shelter,_Encon,_Deighton_Close,_Wetherby_(25th_October_2015).JPG"><em>(image on Wikipedia)</em></a></p>
<p><em>(I won't link embed the image directly)</em></p>
<p>Basically, it's quite similar to a bus shelter, except it's usually equipped with an ashtray, and the roof/cabin thing has no door. When it's closed on all four sides, the entrance is usually a missing panel. Sometimes, it's just a roof with one wall. Around here, they're mainly made of a metal corrugated roof, with glass panels as walls.</p>
<p>The actual defining thing of those shelters, is that it's specifically allowed to smoke in these, while everywhere else it's banned.</p>
<p>Here's how I mapped one of them so far:</p>
<pre><code>amenity=smoking_area
bin=yes
shelter=yes</code></pre>
<p>As they're usually too small to map them as a building, I usually just place a node with the tags above.</p>
<p>I couldn't find an entry on those in the Wiki, so I'm asking here, before I map more of these. The hospital has built around 20-30 of those, next to nearly all buildings there's one or two of those.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shelter" rel="tag" title="see questions tagged &#39;shelter&#39;">shelter</span> <span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '19, 12:17</strong></p>
<img src="https://secure.gravatar.com/avatar/fb7188d8be002ece64870dffe9ec6fa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polemon&#39;s gravatar image" />
<p><span>polemon</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polemon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71344" class="comments-container">
&#10;</div>
<div id="comment-tools-71344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71344-form-container" class="comment-form-container">
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

<span id="71346"></span>

<div id="answer-container-71346" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71346-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="polemon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Edit</strong> -- I've come full circle on this and I'm retracting my previous recommendation. Better to describe the primary purpose first and mention the shelter via subtag:</p>
<p><code>amenity=smoking_area smoking=designated shelter=yes</code></p>
<p>Sorry for the about-face, which breaks the structure of this site. Please adjust your up and downvotes accordingly! ;)</p>
<p><code>------ WAS:</code> I'd have probably gone with <code>amenity=shelter + shelter_type=smoking + smoking=designated</code>.</p>
<p>Checking <a href="https://taginfo.openstreetmap.org/keys/?key=shelter_type">taginfo</a>, there are currently 49 uses of <code>shelter_type=smoking</code> (plus 2 uses of <code>shelter_type=smoking_shelter</code>.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '19, 12:49</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '19, 16:21</strong> </span></p>
</div>
</div>
<div id="comments-container-71346" class="comments-container">
<span id="71384"></span>
<div id="comment-71384" class="comment">
<div id="post-71384-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I have a different perspective from the discussion in other ans: In a conflict of <code>amenity=*</code> value, I suppose the dedicated, purposed use as <code>=smoking_area</code> should prevail, just like how we shouldn't add <code>amenity=shelter</code> to every place with a roof. Non-smokers won't treat a smoking area shelter as an <code>amenity=shelter</code> either. There are ~1.5k <code>=smoking_area</code>, 2 magnitude more than <code>shelter_type=smoking</code>. Such a shelter itself should be represented by an appropriate <code>building=*</code> or <code>man_made=*</code> instead.</p>
</div>
<div id="comment-71384-info" class="comment-info">
<span class="comment-age">(30 Oct '19, 19:18)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="71387"></span>
<div id="comment-71387" class="comment">
<div id="post-71387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Personally, as a non-smoker, I wouldn't hesitate to duck into a smoking shelter during a downpour. And as a mapper, I'd be reluctant to tag something that's not an area <code>smoking_area</code>.</p>
<p>I do see the value in having a single tag that can apply to all designated smoking areas/rooms/shelters/etc. I think the best candidate for that tag is <code>smoking=designated</code>.</p>
<p>I could also see the value in restricting <code>amenity=shelter</code> to wilderness shelters and their ilk, and using <code>building</code> or <code>man_made</code> for other shelter-like things. But since the current use and wiki documentation are much broader in scope (public transport shelters, picnic shelters...) it seems odd to exclude the smoking shelters.</p>
</div>
<div id="comment-71387-info" class="comment-info">
<span class="comment-age">(30 Oct '19, 20:22)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="71400"></span>
<div id="comment-71400" class="comment">
<div id="post-71400-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After uneasy dreams, I've come around on this one and revised my answer. The fact that a node is being called an "area", I'll have to just live with. I mean, it's not half as bad as <code>entrance=exit</code>!</p>
<p>Let no one say productive discussion can't take place on help.osm.org, even if that's not what the software's designed for.</p>
</div>
<div id="comment-71400-info" class="comment-info">
<span class="comment-age">(31 Oct '19, 15:41)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="71404"></span>
<div id="comment-71404" class="comment">
<div id="post-71404-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Heh, OK. Well, it's closer to what I've gone with initially. Tagging in general isn't exactly easy, it's something I go back and forth before committing, all the time.</p>
</div>
<div id="comment-71404-info" class="comment-info">
<span class="comment-age">(31 Oct '19, 22:55)</span> <span class="comment-user userinfo">polemon</span>
</div>
</div>
<span id="71416"></span>
<div id="comment-71416" class="comment">
<div id="post-71416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14350/jmapb"></a><a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a> I actually like <code>smoking=designated</code>, but not sure whether that's enough (only <code>area=yes</code> or building/shelter?), and how it fits into the broader picture (at the very least, with other <code>smoking=*</code> values and uses). Cigarette, along with other consumption (eg: e-cig / HNB,cannabis, alcohol, and food &amp; drink in general) could use some tidy up.</p>
</div>
<div id="comment-71416-info" class="comment-info">
<span class="comment-age">(01 Nov '19, 17:40)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="71423"></span>
<div id="comment-71423" class="comment not_top_scorer">
<div id="post-71423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a>: perhaps a better way would have been to write a new answer disagreeing with your old one. (Not sure if you can vote your own answer down though).</p>
</div>
<div id="comment-71423-info" class="comment-info">
<span class="comment-age">(02 Nov '19, 14:17)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="71425"></span>
<div id="comment-71425" class="comment not_top_scorer">
<div id="post-71425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> you can't vote your own answer down but you can ask (here or on IRC) for other people to do so :)</p>
</div>
<div id="comment-71425-info" class="comment-info">
<span class="comment-age">(02 Nov '19, 14:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="71426"></span>
<div id="comment-71426" class="comment not_top_scorer">
<div id="post-71426-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've decided to use this to map smoking shelters for now. So thanks again for answering (and editing) your answer as you did.</p>
</div>
<div id="comment-71426-info" class="comment-info">
<span class="comment-age">(02 Nov '19, 19:28)</span> <span class="comment-user userinfo">polemon</span>
</div>
</div>
</div>
<div id="comment-tools-71346" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-71346-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71348"></span>

<div id="answer-container-71348" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71348-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both your option, using amenity, and that suggested by <a href="https://help.openstreetmap.org/users/14350/jmapb">@jmapb</a> seem acceptable. I personally have reservations about the trend for a huge variety of shelters to be mapped generically: in particular the risk of confusion where shelter locations are needed in mountainous areas for emergencies. The trend is well established, and I imagine some data consumers are now making use of the shelter_type tag. BUT only 55% of all amenity=shelter have a shelter_type tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '19, 13:58</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71348" class="comments-container">
<span id="71349"></span>
<div id="comment-71349" class="comment">
<div id="post-71349-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I guess the question is, what is it first and foremost. A smoking shelter can't really be used for anything, except smoking and perhaps as a temporary shelter against rain and snow, but nothing else (you surely can't sleep in one, etc.). A "shelter" as you described (and the tag <code>shelter=*</code> kinda implies), is the kind you'd use to hang out when making a break while hiking, etc. Hence, I'm not sure I'm happy with what I tagged them with.</p>
</div>
<div id="comment-71349-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 14:34)</span> <span class="comment-user userinfo">polemon</span>
</div>
</div>
<span id="71351"></span>
<div id="comment-71351" class="comment">
<div id="post-71351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Smoking shelters are usually in urban areas. You won't find a smoking shelter in the mountains, so this shouldn't lead to any confusion. Likewise, you won't search for a typical mountain shelter for sleeping in urban areas. So while the <code>shelter_type</code> tag is important and useful I doubt anyone will confuse a smoking shelter for a sleeping shelter if this tag is absent. Still, <code>shelter_type</code> should be added whenever possible.</p>
</div>
<div id="comment-71351-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 14:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="71352"></span>
<div id="comment-71352" class="comment">
<div id="post-71352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In this urban context I feel that most map users probably won't be looking to sleep in a shelter, and that a smoking shelter can serve the purpose of a generic weather shelter in a pinch. So I don't feel it's a damaging form of troll tagging.</p>
<p>In the wilderness I'd tend to be a lot more cautious with the <code>amenity=shelter</code> tag. I'm not a fan of <code>shelter_type=rock_shelter</code> for instance -- it's too subjective. I've seen caves so small and shallow that I could barely fit inside lying down, but still tagged <code>amenity=shelter + shelter_type=rock_shelter</code>. This I consider to be incorrect and potentially dangerous, because many OSM-derived hiking maps show the shelter without regard to the value of the <code>shelter_type</code> subkey.</p>
</div>
<div id="comment-71352-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 14:57)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="71353"></span>
<div id="comment-71353" class="comment">
<div id="post-71353-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Not true anymore, summer mountain restaurants have smoking shelters. These are unlikely to be of use as a bad weather shelter. Generally I think it's a really bad idea that the interpretation of OSM tags should depend on something like urban/rural, flat/mountainous. Either use different tags (my preference) or ensure that shelter_type is always tagged &amp; consumed. A start might be not rendering any amenity=shelter without the shelter_type tag.</p>
</div>
<div id="comment-71353-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 15:26)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="71357"></span>
<div id="comment-71357" class="comment not_top_scorer">
<div id="post-71357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, so what I gather is, I should use <code>amenity=shelter</code>; <code>shelter_type=smoking</code> and not use the <code>bin=yes</code> tag? From my understanding a <code>*=yes</code> denotes an <code>is-a</code> relation. Hence I'm wary of using <code>bin=yes</code>, as in my mind, it denotes "this <em>is a</em> bin", rather "this <em>has</em> a bin". Similarly, you also tag ways as <code>area=yes</code> if it is an area or <code>building=yes</code> if this is a building.</p>
</div>
<div id="comment-71357-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 16:35)</span> <span class="comment-user userinfo">polemon</span>
</div>
</div>
<span id="71359"></span>
<div id="comment-71359" class="comment">
<div id="post-71359-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>*=yes doesn't always carry the same meaning. It depends on the key being used. Some keys, such as building, are typically treated as defining the object carrying that tag. However, there are others that only provide additional information. Some examples of the latter would include oneway=yes on a highway, bench=yes on a bus stop, or bin=yes on a shelter. On their own, none of these tags define what the object is. If one wanted to define an object as representing a trash bin, they would want to use amenity=waste_basket.</p>
</div>
<div id="comment-71359-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 18:23)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="71363"></span>
<div id="comment-71363" class="comment not_top_scorer">
<div id="post-71363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> hmm, ok, I guess I learned something then. However it doesn't feel right, if you know what I mean. this kind of ambiguity. With <code>oneway=yes</code> one might claim it's still an <code>is-a</code> relationship as it defines an attribute ("&lt;way&gt; is a one-way road"). The other ones are kinda confusing (to me), as it denotes features being present or not, which kinda won't sit right with me. But I guess I'll just accept it as a quirk of it.</p>
</div>
<div id="comment-71363-info" class="comment-info">
<span class="comment-age">(28 Oct '19, 23:28)</span> <span class="comment-user userinfo">polemon</span>
</div>
</div>
<span id="71422"></span>
<div id="comment-71422" class="comment not_top_scorer">
<div id="post-71422-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14400/polemon">@polemon</a>: it can sometimes help to think of things like bin=yes and shelter=yes as an interim step to a finer degree of micro-mapping. Most of the time they are fine, but sometimes the tag clashes with an existing 'top-level' tag (i.e., one which is always used for a thing, not adding properties of a thing). A good example of the latter is the combination amenity=fuel with shop=yes (meaning a gas/petrol station also has a shop), whereas shop=yes means "there's a shop here, but I couldn't find out what it sells". With gas stations the usual solution is to map the shop, usually as shop=convenience (or possibly shop=kiosk). I cant see this taking off with bus shelters, however.</p>
</div>
<div id="comment-71422-info" class="comment-info">
<span class="comment-age">(02 Nov '19, 14:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71348" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-71348-form-container" class="comment-form-container">
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

