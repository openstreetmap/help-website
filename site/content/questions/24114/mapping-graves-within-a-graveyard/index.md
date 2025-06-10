+++
type = "question"
title = "Mapping graves within a graveyard?"
description = '''Hi, I do a good deal of genealogy, and some volunteer photography for Findagrave.com. While newer cemetaries have plot maps and administrative offices, I&#x27;ve been finding that the oldest graveyards in my area (Massachusetts) often have little or nothing to help find grave plots and stones.  I&#x27;m think...'''
date = "2013-07-08T23:35:00Z"
lastmod = "2019-03-18T07:10:00Z"
weight = 24114
keywords = [ "cemetary", "gravestone", "tombstone", "graveyard" ]
aliases = [ "/questions/24114" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping graves within a graveyard?](/questions/24114/mapping-graves-within-a-graveyard)

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
<span id="post-24114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24114-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I do a good deal of genealogy, and some volunteer photography for Findagrave.com. While newer cemetaries have plot maps and administrative offices, I've been finding that the oldest graveyards in my area (Massachusetts) often have little or nothing to help find grave plots and stones.<br />
</p>
<p>I'm thinking of mapping the stones in the Old Burial Ground in Arlington, Massachusetts because a) it's small and b) it's next to my church so I'm often there and c) I have a few cousins buried there. The point is to be able to find a grave, given a name (or partial name) and a graveyard -- and possibly, given a location in a cemetary, look up the grave (though that's often unknown in the oldest graveyards, if there's no legible stone).</p>
<p>I haven't turned up any discussion on the forum on how to do this -- just discussion of markers outside graveyards, and a little abortive discussion on war memorials. Is this a reasonable use of OSM? Is there a best way to do it? Would it be better to just use OSM data, but create a seperate map?</p>
<p>Just for reference, here's how the (vast) Mount Auburn cemetary has done it on Google Maps. Try searching on Longfellow between 1886 and 2013, and click on Alice Mary: <a href="http://www.mountauburn.org/map/">http://www.mountauburn.org/map/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cemetary" rel="tag" title="see questions tagged &#39;cemetary&#39;">cemetary</span> <span class="post-tag tag-link-gravestone" rel="tag" title="see questions tagged &#39;gravestone&#39;">gravestone</span> <span class="post-tag tag-link-tombstone" rel="tag" title="see questions tagged &#39;tombstone&#39;">tombstone</span> <span class="post-tag tag-link-graveyard" rel="tag" title="see questions tagged &#39;graveyard&#39;">graveyard</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '13, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/625923ed30f3baba0fe3cfe2ae20d807?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PatriciaJH&#39;s gravatar image" />
<p><span>PatriciaJH</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PatriciaJH has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-24114" class="comments-container">
<span id="24119"></span>
<div id="comment-24119" class="comment">
<div id="post-24119-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Cartinus's and SK53's answers are a good start, but I couldn't find docs or examples of tagging the actual name and birth/death/burial dates of the person(s) in the tomb (which is necessary for a mountauburn-like map).</p>
<p>Could only find a single instance of grave:name/birth/death/etc=* in taginfo, which looks good (except for graves with multiple people), but is as anecdotic as it gets. Any pointers to a more popular tagging scheme, or should we run along with that one ?</p>
</div>
<div id="comment-24119-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 10:13)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="24124"></span>
<div id="comment-24124" class="comment">
<div id="post-24124-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Vincent</span> Click on the Tombs link in my answer. You'll find a link to <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/Tomb_Plugin">the JOSM tomb plugin</a>. Which uses <a href="http://wiki.openstreetmap.org/wiki/Relation:person">a relation of type=person</a> to store the name, data of birth, etc.</p>
<p>Note that I didn't invent this overly complex construction, somebody else did.</p>
</div>
<div id="comment-24124-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 12:06)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="24131"></span>
<div id="comment-24131" class="comment">
<div id="post-24131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@cartinus</span> thanks, wouldn't have tought that I'd need to lookup a josm plugin to get information about a tagging schema. I've updated the wiki to make things more discoverable.</p>
<p>The person relation may seem a bit complicated, but it does solve problems with on-the-node tagging, and has significant usage numbers.</p>
</div>
<div id="comment-24131-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 14:21)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24114" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24114-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="24116"></span>

<div id="answer-container-24116" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24116-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is certainly reasonable to put this data into Openstreetmap. Have a look at the tagging for <a href="http://wiki.openstreetmap.org/wiki/Tag:historic%3Dtomb">tombs</a>.</p>
<p>It is however unlikely that the graves will ever be displayed on the default map. This doesn't mean you (or somebody else) can't make a map or application that works similar as the Mount Auburn one, but with OSM data and tools. The person to build this might get some good ideas for how <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Applications">Overpass Turbo and some other related applications</a> work</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '13, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '13, 00:19</strong> </span></p>
</div>
</div>
<div id="comments-container-24116" class="comments-container">
<span id="24132"></span>
<div id="comment-24132" class="comment">
<div id="post-24132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just so it doesn't get missed: see also the <a href="http://wiki.openstreetmap.org/wiki/Relation:person">person relation</a> to tag who is buried at a particular site.</p>
</div>
<div id="comment-24132-info" class="comment-info">
<span class="comment-age">(09 Jul '13, 14:22)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24116" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24116-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24118"></span>

<div id="answer-container-24118" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24118-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a couple of answers to questions on this site which may be relevant:</p>
<ul>
<li><a href="https://help.openstreetmap.org/questions/22017/how-do-i-tag-a-single-wayside-grave">How do I tag a single wayside grave?</a></li>
<li><a href="https://help.openstreetmap.org/questions/5758/war-cemetery-maps">War Cemetery Maps</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '13, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-24118" class="comments-container">
&#10;</div>
<div id="comment-tools-24118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24118-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24146"></span>

<div id="answer-container-24146" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24146-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a German wiki page about <a href="http://wiki.openstreetmap.org/wiki/Friedhofmapping">Friedhofmapping</a> (graveyard mapping). It suggests tagging them as</p>
<pre><code>  cemetery = grave
  + name = ...
  + wikipedia:subject = ...</code></pre>
<p>That of course is based on the assumption that we only map graves of famous people where we can rely on Wikipedia or Wikidata to supply the birth/death dates, family relationships and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '13, 23:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-24146" class="comments-container">
&#10;</div>
<div id="comment-tools-24146" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24146-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68406"></span>

<div id="answer-container-68406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For an example of a good layout, but looks to be proprietary, <a href="http://emapping.bmcc.nsw.gov.au/connect/analyst/mobile/#/main?mapcfg=Cemetery">http://emapping.bmcc.nsw.gov.au/connect/analyst/mobile/#/main?mapcfg=Cemetery</a> has a good system, search works, display of where, everyone is shown</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '19, 07:10</strong></p>
<img src="https://secure.gravatar.com/avatar/604345ab66497651786c6d0baa90a5ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave%20Rave&#39;s gravatar image" />
<p><span>Dave Rave</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave Rave has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68406" class="comments-container">
&#10;</div>
<div id="comment-tools-68406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68406-form-container" class="comment-form-container">
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

