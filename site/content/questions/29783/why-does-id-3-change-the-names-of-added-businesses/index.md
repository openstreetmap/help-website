+++
type = "question"
title = "[closed] Why does iD 3 change the names of added businesses?"
description = '''I&#x27;ve been adding a lot of business names to a few local shopping centers and noticed some really odd behaviors. It appears to be consistent but makes no sense, so I gotta ask if these are bugs. Even if not bugs, can somebody explain why these things are happening and how to make it stop. Everything ...'''
date = "2014-01-13T04:10:00Z"
lastmod = "2014-01-13T19:51:00Z"
weight = 29783
keywords = [ "ideditor" ]
aliases = [ "/questions/29783" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Why does iD 3 change the names of added businesses?](/questions/29783/why-does-id-3-change-the-names-of-added-businesses)

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
<span id="post-29783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29783-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been adding a lot of business names to a few local shopping centers and noticed some really odd behaviors. It appears to be consistent but makes no sense, so I gotta ask if these are bugs. Even if not bugs, can somebody explain why these things are happening and how to make it stop. Everything I'm about to write has been edited in iD3.</p>
<p>First, I used to not put business types in to OSM, but in iD3 I finally discovered that if you search for "electronics store" or "pharmacy" or "supermarket" or "clothing store" or whatever else, that it appears to help out by customizing the type of store you're naming. But here are the probems I'm finding...</p>
<p>1) If you choose "Restaurant", you then can add the name of the restaurant and optionally the type of cuisine and everything works great. The name of the business does show up on the map, along with a cool fork &amp; knife icon. I just wanted to establish that as the baseline for what I'd normally expect.</p>
<p>2) But if you choose "Pet Store", "Electronics Store", or "Mobile Phone Store" (among others), the iD3 editor automatically appends " - Pet Store" or " - Electronics Store" to the end of the store <em>type</em>, which makes no sense to me because the name of the store and the type of store are totally different values. So for instance if I choose "Electronics Store" and then add the name value of "Best Buy", it automatically shows up at the top as "Best Buy - Electronics Store". OK, here's the most important part: when this happens, the name of the store does not show up on the rendered map, defeating the purpose of adding any of this information to OSM.</p>
<p>3) However if you choose "Clothing Store", it does the same as I described above, adding " - Clothing Store" after the name, but in this case clothing stores do actually show up on the map. Weird that it's inconsistent like that.</p>
<p>4) Finally, for "Sporting Goods Store", "Jeweler", "Shoe Store" and some others, it doesn't do that automatic name changing thing, but none of these types of stores will show up on the rendered map at all.</p>
<p>So what the heck is the deal with these things? I used to just do "business" and name and it worked. You'd think that adding the type of business would be more helpful but it is so often preventing it from showing up on the rendered OSM maps. Please explain this madness before I bother to add more and more business names all over the world.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '14, 04:10</strong></p>
<img src="https://secure.gravatar.com/avatar/228a09e620f374c61a25e546d76bc6a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopanthers&#39;s gravatar image" />
<p><span>gopanthers</span><br />
<span class="score" title="366 reputation points">366</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopanthers has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>13 Jan '14, 20:00</strong> </span></p>
</div>
</div>
<div id="comments-container-29783" class="comments-container">
<span id="29784"></span>
<div id="comment-29784" class="comment">
<div id="post-29784-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>These are two different issues. One is about rendering, probably on osm.org. This is a conflict between showing all possible information and stil having a readable map, a lots of questions and answers are already given here.</p>
<p>The second is about what iD does with business names. As this is a new issue, I've geared the question towards this.</p>
</div>
<div id="comment-29784-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 07:37)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
<span id="29785"></span>
<div id="comment-29785" class="comment">
<div id="post-29785-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your point "2" is based on a wrong assumption. The purpose of adding something to OSM is <em>not</em> defeated by it not showing up on the default openstreetmap.org map. Firstly, there are myriad other maps based on our data which may decide to show the object. Secondly, a lot of software allows you to search for objects ("find nearby electronics store") and for that, even a "Best Buy" not showing on the map makes sense!</p>
</div>
<div id="comment-29785-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 07:47)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="29788"></span>
<div id="comment-29788" class="comment">
<div id="post-29788-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Odd. I've just added an electronics store to the dev server as a test and I don't get " - Electronics Store" appended to the end of the store type:</p>
<p><a href="http://api06.dev.openstreetmap.org/node/4295810899">http://api06.dev.openstreetmap.org/node/4295810899</a></p>
<p>Maybe you could provide an example of one that you added that did (to compare editor versions, etc.).</p>
</div>
<div id="comment-29788-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 09:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="29805"></span>
<div id="comment-29805" class="comment">
<div id="post-29805-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here's a link to one of the shopping centers I've been seeing this in. <a href="https://www.openstreetmap.org/#map=17/35.10269/-80.98677">https://www.openstreetmap.org/#map=17/35.10269/-80.98677</a> You'll notice when editing that the building on the east side has a Best Buy on one end and a PetSmart on the opposite end (neither of which show up on rendered OSM). Those two stores are examples of ones that iD3 has changed the title of the tag to include both the type and the name together. Also towards the middle of the shopping center there's also a Kay Jeweler and an Omega Sports which also don't show up either, but those don't do the renaming thing.</p>
</div>
<div id="comment-29805-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 14:32)</span> <span class="comment-user userinfo">gopanthers</span>
</div>
</div>
<span id="29806"></span>
<div id="comment-29806" class="comment">
<div id="post-29806-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@gopanthers</span> please read my answer ... you are confusing a pure graphical layout "issue" with what is actually tagged on the object.</p>
</div>
<div id="comment-29806-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 14:39)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="29811"></span>
<div id="comment-29811" class="comment not_top_scorer">
<div id="post-29811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand how the information can still be useful to a variety of other mapping systems. I think it's annoying that certain business types don't show up on the OSM render because it encourages me to enter less information (if I just said "building" and the name only, then it will show up), but I do realize that other map applications can use it.</p>
<p>But what's confusing me more is the odd behavior with iD3 automatically appending the name of the business to the data type (it may be called a "key") for some types of businesses but not others.</p>
</div>
<div id="comment-29811-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 19:14)</span> <span class="comment-user userinfo">gopanthers</span>
</div>
</div>
<span id="29812"></span>
<div id="comment-29812" class="comment not_top_scorer">
<div id="post-29812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>iD isn't appending the name of the business to the key - the "name" is still "Best Buy". But iD has a preset called "Best Buy - Electronic Store" which is displayed at the top-left of the screen in iD when you've selected that preset.</p>
<p>As has been mentioned elsewhere, the name of the node that you added is just "Best Buy":</p>
<p><a href="https://www.openstreetmap.org/node/2619349389">https://www.openstreetmap.org/node/2619349389</a></p>
</div>
<div id="comment-29812-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 19:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29783" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-29783-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by gopanthers 13 Jan '14, 20:00

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29787"></span>

<div id="answer-container-29787" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29787-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As has already been pointed out if a added point of interest is visible on the "standard" map depends on many factors and should never control if you should add a feature or not.</p>
<p>What is confusing you in adding the stores is that iD has two slightly different ways of supporting adding features, on the one hand it has "presets" for different types of facilities (restaurants, electronics stores etc), on the other hand it has a predifined list of names and and corresponding feature types to avoid typos and different tagging for shops or facilities of the same chain.</p>
<p>Good example is "Best Buy": if you enter it as a name or search for it, iD will automatically use the predefined entry for the Best Buy chain of stores, that is what the list entry "Best Buy - Electronics Store" is indicating. If you check you will see that the name value is actually only set to "Best Buy" as it should be.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '14, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jan '14, 12:19</strong> </span></p>
</div>
</div>
<div id="comments-container-29787" class="comments-container">
&#10;</div>
<div id="comment-tools-29787" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29787-form-container" class="comment-form-container">
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

