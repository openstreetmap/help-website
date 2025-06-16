+++
type = "question"
title = "Tagging public footpaths for routing"
description = '''I&#x27;m an OSM beginner. My focus has been recently on adding public footpaths in my area, and I&#x27;ve been frustrated over the confusing guidelines for tagging them. I&#x27;ve retagged paths a number of times as I&#x27;ve found differing advice on how to do this: highway=path or footway, foot=yes or designated, plu...'''
date = "2011-08-11T08:17:00Z"
lastmod = "2011-08-26T22:20:00Z"
weight = 7015
keywords = [ "footpath", "public", "tagging", "routing" ]
aliases = [ "/questions/7015" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging public footpaths for routing](/questions/7015/tagging-public-footpaths-for-routing)

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
<span id="post-7015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7015-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-7015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm an OSM beginner. My focus has been recently on adding public footpaths in my area, and I've been frustrated over the confusing guidelines for tagging them. I've retagged paths a number of times as I've found differing advice on how to do this: highway=path or footway, foot=yes or designated, plus designated= <em>and access=</em> possibly. The clearest advice I've found is in the <a href="https://wiki.openstreetmap.org/wiki/UK_public_rights_of_way#Public_footpath">UK PROW guidelines</a> which recommends:</p>
<blockquote>
<p>highway=path;foot=designated;designation=public_footpath (global style)</p>
</blockquote>
<p>This is what I'm following. However, among other advice I found this <a href="http://forum.openstreetmap.org/viewtopic.php?id=8406">forum entry</a> from two senior members that recommends the use of footway over path. At the risk of opening a can of worms that's probably been opened many times before, can someone confirm that the advice I'm following is the best? What do I need to use to get ORS (<a href="http://OpenRouteService.org">OpenRouteService.org</a>) to used my paths for pedestrian routing because at the moment it's not. The advice on <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">tagging for routing</a> indicates that what I'm using should be OK.</p>
<p>Also, I find the meaning of "designated" confusing. Again, under <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">Access-Restrictions</a> the value "designated" is described as "same as yes but this road can optionally be prefered by some of your metrics" i.e. a preferred route. However, in the PROW guidelines it's used to indicate a legal status i.e. specifically a PROW (even though this is also defined by the designation tag) - at least I assume this is what it means here. If so, I can't use this tagging to indicate any routing preference for using the path. This would be useful because public paths come in all varieties, from the pleasant and easy, to mudbaths and infrequently-used overgown jungles. You would want routing to use the first, but probably not the second. Could tracktype do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-footpath" rel="tag" title="see questions tagged &#39;footpath&#39;">footpath</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '11, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/660363689cead9b16bfce059d49fe7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceperman&#39;s gravatar image" />
<p><span>ceperman</span><br />
<span class="score" title="291 reputation points">291</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceperman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7015" class="comments-container">
<span id="7354"></span>
<div id="comment-7354" class="comment">
<div id="post-7354-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I initially found the designated term odd.But an example is that if access is limited to say walkers or horses, then they are the "designated" exceptions so access designated to the various exceptions</p>
</div>
<div id="comment-7354-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 22:20)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-7015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7015-form-container" class="comment-form-container">
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

<span id="7064"></span>

<div id="answer-container-7064" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7064-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think it's worth looking at the history of these tags.</p>
<p><code>highway=footway</code> long pre-dates <code>highway=path</code> and was originally intended for both asphalt paths in towns and footpaths in the countryside. Paths that were cycleable were cycleways (in other words there was a hierarchy, with footway as the lowest common denominator of most of the other <code>highway=*</code> tags, motorway being the obvious exception). There are numerous discussions in the mail archives on these points.</p>
<p>Access tags followed: for obvious reasons. There are many usable paths where the access rights are not shown on most maps and adding this information to OSM was useful. Furthermore different countries have different default access regulations for things like cycle tracks.</p>
<p>A particular problem was defining the legal status of public rights of way in England and Wales. At the outset the original highway tags were adequate, but over time it became clear that something else was needed. After a number of false starts (using access tags) the designation tag arrived and seems to work well.</p>
<p>So what does this mean for path versus footway? There are basically three interpretations of path:</p>
<ol>
<li>A footpath in the countryside (widely used in Germany). In this scheme footway is only used for asphalt paths in towns. In practice this distinction can also be achieved by using the <code>surface</code> tag.</li>
<li>A multi-access path: where no single use can be defined which suitably incorporates other uses (this is pretty much the description on the <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dpath">wiki</a>).</li>
<li>A path which was not ground surveyed and insufficient information is available about access (by analogy with highway=road).</li>
</ol>
<p>Generally, then it is best to see what standard has emerged locally for mapping these things.</p>
<p>In the UK usage has oscillated, but the two mappers I would regard as standard setters for footpath mapping (<a href="https://www.openstreetmap.org/user/nickw">Nickw</a> and <a href="https://www.openstreetmap.org/user/SomeoneElse">SomeoneElse</a>) both prefer highway=footway. The wiki advice regarding footpath mapping (global style) represents the point of view of one individual <strong>NOT</strong> the consensus of mappers in the UK: in practice, <code>highway=footway</code> has a clear meaning and <code>highway=path</code> does not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '11, 11:13</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7064" class="comments-container">
<span id="7235"></span>
<div id="comment-7235" class="comment">
<div id="post-7235-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You are mentioning several times "asphalt" which is a surface property and should therefore go into the "surface" tag. This has nothing to do with footway vs. path. Also in cities and towns (and also in Germany) the surface of a footway can be unpaved (actually in parks it often is).</p>
</div>
<div id="comment-7235-info" class="comment-info">
<span class="comment-age">(21 Aug '11, 10:59)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-7064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7064-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7134"></span>

<div id="answer-container-7134" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7134-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SK53: I appreciate the insight you provided, but I have a number of problems with it.</p>
<p>You say that the wiki advice regarding mapping PROW that I referred to represents an individual's view and not a consensus. How I'm supposed to know this? This is a problem I have continally with OSM. <em>All</em> the advice about tagging is in the wiki, so how is one to distinguish between accepted standards and individual views? In the case of the PROW page, it's linked to (via Deprecated Features) from the main Map Features page so it has all the appearance of being approved advice. If the view of the two you mentioned is now considered "the consensus", shouldn't someone update the PROW page?</p>
<p>Personally I don't like "designated" because it's described and used inconsistently. Why not use the existing value "offical" which seems to fit the bill? Also, for "footway" I think I'm with the Germans on this. It suggests an official, surfaced footpath, and not a rough path in the countryside that it's possible to walk along. Adding foot=* is all that's needed to explicitly indcate the "footness" of the way. Footway suggests something more that footpath.</p>
<p>For me, all this highlights a general issue with OSM - the lack of clearly defined and documented tagging standards. I really don't understand how OSM data can be meaningfully created and interpreted without such definition. I'm sure that, initially at least, mappers would prefer to be told how to tag their data rather than having to judge between various alternatives based on no experience whatsoever.</p>
<p>As for the question at hand, I'll go with any consensus there is - just as long as I know what it is. And I'm really still not sure.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '11, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/660363689cead9b16bfce059d49fe7d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceperman&#39;s gravatar image" />
<p><span>ceperman</span><br />
<span class="score" title="291 reputation points">291</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceperman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7134" class="comments-container">
<span id="7150"></span>
<div id="comment-7150" class="comment">
<div id="post-7150-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>There is exactly this problem with the wiki: it tends to become a soap-box for how some people think tags should be used. Many of us regard the tag approval/voting process as broken because it rarely reflects a true consensus (15 votes in a project with 10'000s of people mapping is a drop in the ocean).</p>
<p>It is much better to use the tag usage tools (taginfo, tagwatch) to see how a tag is used in practice. Most wiki pages link to these.</p>
<p>The rest of your points are too philosophical for here: suffice it say OSM seems to work pretty well without formal guidelines.</p>
</div>
<div id="comment-7150-info" class="comment-info">
<span class="comment-age">(17 Aug '11, 11:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="7236"></span>
<div id="comment-7236" class="comment">
<div id="post-7236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Probably you can get the most settled advice through the mapping features and related "key" and "tag" pages. All country specific pages might be less universally useful. All pages like "how to tag a ..." and others might be less often looked at and therefore might contain either more subjective and or less up to date information.</p>
<p>If you are in doubt feel free to ask on the mailing lists. Even if there will not necessarily be a consensus you will get to know the different arguments to decide yourself.</p>
</div>
<div id="comment-7236-info" class="comment-info">
<span class="comment-age">(21 Aug '11, 11:03)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="7244"></span>
<div id="comment-7244" class="comment">
<div id="post-7244-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just as SK53 says. Ignore the wiki. Use the tag usage tools, and trust your editor's presets.</p>
</div>
<div id="comment-7244-info" class="comment-info">
<span class="comment-age">(21 Aug '11, 22:25)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="7265"></span>
<div id="comment-7265" class="comment">
<div id="post-7265-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@ceperman</span> I am with you. The wiki voting process is non representative. The problem is the consensus finding. Currently it works, because obviously the most used tags are the consensus. But in the future it would be nice to have some sort of LiquidDemocracy/Proxy voting for this.</p>
</div>
<div id="comment-7265-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 18:07)</span> <span class="comment-user userinfo">Flow</span>
</div>
</div>
<span id="7275"></span>
<div id="comment-7275" class="comment">
<div id="post-7275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Richard</span> AFAIKS tag usage tells you what's being used, but not what was meant by the tagger. I'm not sure how this helps. Using editor presets is probably the best advice, except JOSM only offers "dedicated footway" for footpaths, thus back to the footway debate, and the symbol it shows for this preset seems to agree with my interpretation of footway and doesn't encourage its use for rural footpaths.</p>
<p>There seems to be no clear answer to my question, and this doesn't seem the right place for protacted discussion. So I'm going to leave it there and continue if necessary in the mailing lists.</p>
</div>
<div id="comment-7275-info" class="comment-info">
<span class="comment-age">(23 Aug '11, 16:55)</span> <span class="comment-user userinfo">ceperman</span>
</div>
</div>
</div>
<div id="comment-tools-7134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7134-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7044"></span>

<div id="answer-container-7044" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7044-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Remember when using <em>footway</em> you disallow bicycles unless allowing them explicitly with <em>bicycle=yes</em> and when using <em>cycleway</em> you disallow pedestrians unless allowing them explicitly with <em>foot=yes</em> whereas when using <em>path</em> you allow both of them. However, these access restrictions also depend on the country, see <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">access restrictions</a> page in the wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '11, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7044" class="comments-container">
<span id="7243"></span>
<div id="comment-7243" class="comment">
<div id="post-7243-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In most countries, and for most applications consuming OSM data, highway=cycleway implies pedestrian access.</p>
</div>
<div id="comment-7243-info" class="comment-info">
<span class="comment-age">(21 Aug '11, 22:25)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="7247"></span>
<div id="comment-7247" class="comment">
<div id="post-7247-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not a safe assumption. Path implies both, cycleway implies pedestrians excluded. When in doubt, explicitly tag.</p>
</div>
<div id="comment-7247-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 06:52)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="7248"></span>
<div id="comment-7248" class="comment">
<div id="post-7248-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thousands of miles of cycleway in the UK rather disagree with you.</p>
</div>
<div id="comment-7248-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 07:35)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="7249"></span>
<div id="comment-7249" class="comment">
<div id="post-7249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>UK access permissions don't apply to the rest of the world. The mentioned wiki page clearly says that cycleway forbids pedestrian access by default as well as in several countries, e.g. France, Germany, Hungary, ...</p>
</div>
<div id="comment-7249-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 07:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7252"></span>
<div id="comment-7252" class="comment">
<div id="post-7252-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>UK access permissions do, however, apply to this question, since that's exactly what the questioner was asking about.</p>
</div>
<div id="comment-7252-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 10:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="7338"></span>
<div id="comment-7338" class="comment not_top_scorer">
<div id="post-7338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span></span><span>@Paul Johnson</span> I understand that path actually implies nothing. However, "When in doubt, explicitly tag" - that's good advice.</p>
</div>
<div id="comment-7338-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 10:51)</span> <span class="comment-user userinfo">ceperman</span>
</div>
</div>
</div>
<div id="comment-tools-7044" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-7044-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7039"></span>

<div id="answer-container-7039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7039-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-7039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There has been no consensus to date on when to use path vs footway vs cycleway. I'd say if it's used (almost) exclusively for pedestrians, use footway. If it's used (almost) exclusively for bicycles, use cycleway. If it's more of a mix, use path.</p>
<p>I'd say the best advice is to be consistent in a given area, and to be sure routers use the data correctly tag foot/bicycle=yes/permissive/designated. This way routers can rely on those access tags rather than on highway=path/cycleway/footway.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '11, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ba99ad3778972fee07700e1eb36cc822?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoshD&#39;s gravatar image" />
<p><span>JoshD</span><br />
<span class="score" title="300 reputation points">300</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoshD has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-7039" class="comments-container">
&#10;</div>
<div id="comment-tools-7039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7039-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7017"></span>

<div id="answer-container-7017" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7017-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-7017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Footway × Path</strong> I see footway as a paved way for pedestrians intentionally built in the place where it is (pleasant and easy), and path as something that appeared because people are going there (mudbaths and infrequently-used overgown jungles). But this is probably my subjective view, that might be partially based by icons used for this in JOSM. :)<br />
Tracktype should go with track and I am not aware of any "pathtype" equivalent.</p>
<p><strong>Routing</strong> I would not rely on openrouteservice for routing - it apparently does not update very often and currently it uses data from 20. 05. 2011 for routing. (I got that <a href="/questions/6035/routing-not-working-properly">problem</a> with my first edit...)</p>
<p>The <strong>access restrictions</strong> are confusing indeed. I am not if the tag mean physical possibility of going somewhere, legal possibility of going somewhere or its combination. After all the access restrictions correspond much more to common-law system than continental.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '11, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-7017" class="comments-container">
<span id="7262"></span>
<div id="comment-7262" class="comment">
<div id="post-7262-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In your path/footway description you don't address the issue of UK footpaths. They are grass/mud paths in the countryside which are officially registered and signed. Sometimes they are overgrown because the landowner/local authority hasn't bothered to maintain them correctly.</p>
</div>
<div id="comment-7262-info" class="comment-info">
<span class="comment-age">(22 Aug '11, 14:56)</span> <span class="comment-user userinfo">quantumstate</span>
</div>
</div>
<span id="7333"></span>
<div id="comment-7333" class="comment">
<div id="post-7333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Adding to quantumstate comment putting these paths on our map hopefully will get them walked more, which will hopefully keep them clearly defined on the ground by treading down vegetation, especially in times when local authorities and land owners have other priorities</p>
</div>
<div id="comment-7333-info" class="comment-info">
<span class="comment-age">(26 Aug '11, 09:10)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-7017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7017-form-container" class="comment-form-container">
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

