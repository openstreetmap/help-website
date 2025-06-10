+++
type = "question"
title = "Tagging shops, what are the risks?"
description = '''I&#x27;m a new contributor to OSM (and I love it). Recently, I noticed how often people tag differently the same kind of shops and I&#x27;m wondering what could be the consequences of that. Because when I think about OSM, I think - and hope - that GPS devices will eventually be able to use those tags/keywords...'''
date = "2012-06-13T06:14:00Z"
lastmod = "2013-05-11T09:39:00Z"
weight = 13487
keywords = [ "different", "tag", "standards", "consequences", "tags" ]
aliases = [ "/questions/13487" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Tagging shops, what are the risks?](/questions/13487/tagging-shops-what-are-the-risks)

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
<span id="post-13487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13487-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-13487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm a new contributor to OSM (and I love it). Recently, I noticed how often people tag differently the same kind of shops and I'm wondering what could be the consequences of that.</p>
<p>Because when I think about OSM, I think - and hope - that GPS devices will eventually be able to use those tags/keywords and give you a list of specific shops close to where you are, even their addresses. But what will happen if some people think that a place where you buy pets is tagged shop=pets and shop=animals by some other people? I doubt that the GPS will guess that those two shops belong to the same "category"...</p>
<p>So, I try to use the wiki as much as I can, to tag the shops by using taginfo, but I sometimes wonder wether the OSM community should be more strict about the tagging process. After all, it's good to get data, but it's better if computer/GPS/anything can use it!</p>
<p>I'm sure the tagging system is not finished and that it will be more accurate in a near future, but I hope we don't do anything that we will have to do again considering that some tags might be modified in the future.</p>
<p>I just wanted to share that with you, that's it!</p>
<p>Thank you all for your support, OSM is a great project, the quality of our work will make the difference when Apple and Google will improve their maps. But I'm convinced that we can do better than them!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-different" rel="tag" title="see questions tagged &#39;different&#39;">different</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-standards" rel="tag" title="see questions tagged &#39;standards&#39;">standards</span> <span class="post-tag tag-link-consequences" rel="tag" title="see questions tagged &#39;consequences&#39;">consequences</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jun '12, 06:14</strong></p>
<img src="https://secure.gravatar.com/avatar/b06617c36d7035085a5940ead56c5219?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hugues%20F&#39;s gravatar image" />
<p><span>Hugues F</span><br />
<span class="score" title="391 reputation points">391</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hugues F has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13487" class="comments-container">
&#10;</div>
<div id="comment-tools-13487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13487-form-container" class="comment-form-container">
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

<span id="13500"></span>

<div id="answer-container-13500" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13500-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hugues F has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When using OSM data in a navigation system you will most probably not be using the raw data but a subset, which is usually more or less normalized. If shop=pets and shop=animals do have the same or very similar meaning, then the person that converts OSM data into data for your device will probably put them into the same category.</p>
<p>It is not important at all, that all the mappers use the same tags to describe the same thing of the real world. But it is very important that a tag is always used with the same intended meaning. If the latter is not the case, then the tag is almost useless, while the first has no negative implications at all besides from being more work to interpret the data.</p>
<p>Using taginfo to find tags that are not documented in the wiki is generally a bit problematic, because you can only guess about the intended meaning. Taginfo is a great tool to estimate the importance and diffusion of a tag, but finding new ones that are not documented bears some risk. You'd better ask on the lists or directly the mappers what might be the intended meaning (but still you will not be sure in many cases that all mappers who used an undocumented tag had all the same intentions).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '12, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '12, 16:34</strong> </span></p>
</div>
</div>
<div id="comments-container-13500" class="comments-container">
<span id="13504"></span>
<div id="comment-13504" class="comment">
<div id="post-13504-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ok, so I should always check the wiki first, then Taginfo. If nothing seems to fit, I'll ask my question here.</p>
<p>Thanks.</p>
</div>
<div id="comment-13504-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 17:31)</span> <span class="comment-user userinfo">Hugues F</span>
</div>
</div>
</div>
<div id="comment-tools-13500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13500-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13505"></span>

<div id="answer-container-13505" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13505-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-13505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You said:</p>
<blockquote>
<p>I think - and hope - that GPS devices will eventually be able to use those tags/keywords and give you a list of specific shops close to where you are, even their addresses.</p>
</blockquote>
<p>In some places, that's pretty much where we are now. Taking one example, Garmin handhelds and satnavs work well with maps created from OSM data, and <a href="http://www.mkgmap.org.uk/">mkgmap</a>, which is used to create Garmin maps, allows you to map pretty much any OSM tag into any pretty much Garmin feature. If I'm out in the wilds of Derbyshire and want to find a pub that serves decent beer and has a stone floor so that I don't need to take my boots off I can very easily do that.</p>
<blockquote>
<p>But what will happen if some people think that a place where you buy pets is tagged shop=pets and shop=animals by some other people?</p>
</blockquote>
<p>With some features, that's also where we are now. How different to me is a highway=footway from a highway=path;foot=yes? What about natural=wood vs landuse=forest? If the difference isn't important to whoever's creating the map they will probably just map them to the same map feature, so that if you search for "pet shop" you'll get all widely used tags for that item.</p>
<p>OSM has traditionally said that you can use <a href="http://wiki.openstreetmap.org/wiki/Any_tags_you_like">any tags you like</a> - it removes a barrier to new contributors, and the more people mapping, the better the map. If someone adds a "shop=iguana" someone else can come along and change it to "shop=pet;pet=iguana" without losing any of the original meaning. If a rigid hierarchy for tags was enforced they'd probably never have mapped it in the first place. Another problem that a rigid tagging scheme would have is that the world is a big place and it's impossible to extrapolate from one local area to the rest of the world - I've never been to Outer Mongolia and I'm sure there are things that mappers there think are quite important that I've not clue about, so best to leave Outer Mongolia mappers to choose their own tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '12, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13505" class="comments-container">
<span id="13507"></span>
<div id="comment-13507" class="comment">
<div id="post-13507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you change an object from "shop=iguana" to "shop=pet;pet=iguana" you might loose some meaning. It is not obviously the same. An object tagged with "shop=iguana" seems to me a shop only selling iguana, or at least specialized in iguana, while the combination bears a high risk to be misinterpreted as general pet shop (because pet=iguana is likely to be not evaluated). But also if you tried to interpret it you cannot really be sure if this is a iguana-only shop or if they also sell fish and cat food (i.e. they have besides other stuff also iguana).</p>
</div>
<div id="comment-13507-info" class="comment-info">
<span class="comment-age">(13 Jun '12, 18:00)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-13505" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13505-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13502"></span>

<div id="answer-container-13502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13502-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, this help tool is normally for questions, not for comments... but thank you for your support about the project.</p>
<p>About "shop=pets" or "shop=animals", you can see on the wiki that the recommended tag is "<a href="http://wiki.openstreetmap.org/wiki/Tag:shop%3Dpet">shop=pet</a>". You mentionned the wiki and taginfo. The wiki tries to define a consensus about tagging. Taginfo shows statistics about real usage. But both have pros and cons: the OSM wiki is not very well structured and maintained. Taginfo on the other side is showing the amount of instances of a certain tag, also tags combination which is nice. But it does not say if the usage is consistent worlwide or if the tag is used by a single person hundreds times or by hundreds persons a single time. And stats can be distorted by mass imports.</p>
<p>Currently, taginfo says 2527 "<a href="http://taginfo.openstreetmap.org/search?q=shop%3Dpet">shop=pet</a>", 67 "<a href="http://taginfo.openstreetmap.org/search?q=shop%3Dpets">shop=pets</a>", 3 "<a href="http://taginfo.openstreetmap.org/search?q=shop%3Danimal">shop=animal</a>" and 10 "<a href="http://taginfo.openstreetmap.org/tags/shop=animals">shop=animals</a>". It seems that most of the contributors follow the wiki recommendations but we cannot avoid that some people use their creativity (or laziness) and use a new tag. Best we can do here is to check and fix the wrong tags. Monitoring is also easier with the help of some <a href="http://wiki.openstreetmap.org/wiki/Quality_assurance">QA tools</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '12, 16:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '12, 16:53</strong> </span></p>
</div>
</div>
<div id="comments-container-13502" class="comments-container">
&#10;</div>
<div id="comment-tools-13502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14205"></span>

<div id="answer-container-14205" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14205-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Answering just the heading 'What is the risk of tagging shops', I have a different slant on the basis that some shops (especially the name and type of it) change quite regularly compared to the geographic feature of just the building.</p>
<p>There is of course an on going data maintainance activity as these features change, so there's quite a risk of the data being out of date if there are not a sufficient number of local mappers to notice those changes.</p>
<p>I suppose I try to map what I think/find is the most 'useful' or interesting features first, each to their own of course.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '12, 00:52</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14205" class="comments-container">
&#10;</div>
<div id="comment-tools-14205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14205-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22299"></span>

<div id="answer-container-22299" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22299-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-22299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>[spam removed]</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '13, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/5bcf2bb2c1ce975eb8efa7ecea20a2a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shanewatson5&#39;s gravatar image" />
<p><span>shanewatson5</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shanewatson5 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '13, 10:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-22299" class="comments-container">
&#10;</div>
<div id="comment-tools-22299" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22299-form-container" class="comment-form-container">
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

