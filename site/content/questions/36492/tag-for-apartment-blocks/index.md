+++
type = "question"
title = "Tag for apartment blocks?"
description = '''An apartment complex may contain a large amount of different buildings, all of them with the same street address. The only thing that differentiates them is the number of the apartment block or the range of apartment numbers within each of them. Is there a specific tag for that?'''
date = "2014-09-02T04:56:00Z"
lastmod = "2014-09-08T04:36:00Z"
weight = 36492
keywords = [ "building", "apartment", "block", "tagging" ]
aliases = [ "/questions/36492" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Tag for apartment blocks?](/questions/36492/tag-for-apartment-blocks)

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
<span id="post-36492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36492-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>An apartment complex may contain a large amount of different buildings, all of them with the same street address. The only thing that differentiates them is the number of the apartment block or the range of apartment numbers within each of them.</p>
<p>Is there a specific tag for that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-apartment" rel="tag" title="see questions tagged &#39;apartment&#39;">apartment</span> <span class="post-tag tag-link-block" rel="tag" title="see questions tagged &#39;block&#39;">block</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '14, 04:56</strong></p>
<img src="https://secure.gravatar.com/avatar/552d28190b10de4eb02f7e0891aefa5d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xoko&#39;s gravatar image" />
<p><span>xoko</span><br />
<span class="score" title="75 reputation points">75</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xoko has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-36492" class="comments-container">
&#10;</div>
<div id="comment-tools-36492" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36492-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="36506"></span>

<div id="answer-container-36506" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36506-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-36506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Andy MacKey says, draw each building as a polygon and tag with <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dapartments"><code>building=apartments</code></a> to show that this is what the original purpose of the building (other tags may be appropriate, such as <a href="http://taginfo.openstreetmap.org/tags/building%3Ause=apartments"><code>building:use=apartments</code></a> if the building was originally built for another purpose, such as a factory, warehouse or church).</p>
<p>If the area of the apartment complex is widely known, and/or signposted as such, then you can also create a landuse=residential polygon and add the name of the complex to that polygon (example <a href="http://www.openstreetmap.org/way/40448227">here</a>).</p>
<p>If the name is not widely used, or only used in an address context, then just use this on address nodes. The preferred way to map addresses for apartments is to add them to a node which is the main entrance of the building (tag entrance=main). A typical combination will be <code>addr:flats=1-n; addr:interpolation=all; addr:housename=Complex Name; addr:street=Main Street</code>. The details of this have recently been discussed on the <a href="https://lists.openstreetmap.org/pipermail/tagging/2014-August/018888.html">tagging list</a>, specifically the use of the interpolation tag for flats. There is good additional information from experienced address mappers in the posts.</p>
<p>Note that addr:flats is not shown on the main Carto (aka Mapnik) map style, the housenumber or name is instead. However the data are there and usable.</p>
<p>I have documented some of this on the wiki at <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dapartments">building=apartments</a> (including an example of a <a href="http://www.openstreetmap.org/way/158513353">converted church</a>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '14, 08:17</strong> </span></p>
</div>
</div>
<div id="comments-container-36506" class="comments-container">
<span id="36507"></span>
<div id="comment-36507" class="comment">
<div id="post-36507-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Recently, I saw the advice to use name instead of addr:housename for 99% of the cases (here on this help forum). Is this one of the 1% ? Or do you have a different opinion about that issue ? (no critique, just want to know).</p>
<p>Furthermore IMHO the addr:interpolation is for addr:housenumber, not for addr:flats.</p>
</div>
<div id="comment-36507-info" class="comment-info">
<span class="comment-age">(02 Sep '14, 15:16)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="36525"></span>
<div id="comment-36525" class="comment">
<div id="post-36525-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This was recently discussed on talk-tagging, by users who have mapped 10,000s of buildings. The use of addr:interpolation on nodes with addr:flats has a fairly long history, is unambiguous and highly useful. Alternatives such as mapping every apartment as a separate node are often less useful (e.g., for routing where the front door is the destination). Requiring an additional interpolation tag for flats and units seems overkill.</p>
</div>
<div id="comment-36525-info" class="comment-info">
<span class="comment-age">(02 Sep '14, 20:53)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36539"></span>
<div id="comment-36539" class="comment">
<div id="post-36539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can it be unambiguous when you have addr:housenumber=67-75, addr:flats=1=100, on the same node ?</p>
<p>In such case one would need addr:interpolation=odd for the housenumbers and all for the flats ... I just assume somewhere in the world such an example exists.</p>
<p>Furthermore the wiki states for addr:interpolation "How to interpolate the house numbers belonging to the way along the respective street. " So please update the documentation on the wiki when it can be used for addr:flats (and perhaps addr:units) as well. (<a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a> )</p>
</div>
<div id="comment-36539-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 06:11)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="36546"></span>
<div id="comment-36546" class="comment">
<div id="post-36546-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Because 67-75 is a single address with no interpolation, the interpolation must always apply to the finer grade unit: at least all the cases we've come across fall into this scope (~80,000 addresses mapped). I've stated before I put actual usage way ahead of descriptions on the wiki. I have added stuff for building=apartments.</p>
</div>
<div id="comment-36546-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 09:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36563"></span>
<div id="comment-36563" class="comment not_top_scorer">
<div id="post-36563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>SK53, could you show me an example, to check if I have understood well what you just said?</p>
</div>
<div id="comment-36563-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 17:01)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
<span id="36586"></span>
<div id="comment-36586" class="comment not_top_scorer">
<div id="post-36586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think newbies (at least I did) look at the wiki to learn something, they do not try to learn from studying 80000 addresses and try to guess what the previous mapper intended with some key-value combinations. Not to mention how they can find such examples.</p>
<p>Key concepts like address mapping need to be in the wiki and need to be correct.</p>
<p>So when does a geocoder has to return the above node (tagged as 67-75) ? Only when the search request is 67-75 ? or also when it is 67, 68, ... 75 ? (when the addr:interpolation is for the finer unit)</p>
</div>
<div id="comment-36586-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 07:14)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="36644"></span>
<div id="comment-36644" class="comment not_top_scorer">
<div id="post-36644-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, SK53. So I must specify the address only in the main entrance of the apartment complex. But my question still remains there. How do I differentiate the buildings of the apartment complex? The only difference is the apartment numbers. Must I specify the apartment numbers?</p>
</div>
<div id="comment-36644-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 04:27)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
<span id="36646"></span>
<div id="comment-36646" class="comment not_top_scorer">
<div id="post-36646-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that's what he writes, yes, using addr:flats.</p>
</div>
<div id="comment-36646-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 07:55)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="36649"></span>
<div id="comment-36649" class="comment not_top_scorer">
<div id="post-36649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One point about addr:flats is that it does not render, but is searchable. I've added this to the answer.</p>
</div>
<div id="comment-36649-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 08:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36673"></span>
<div id="comment-36673" class="comment">
<div id="post-36673-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It seems that my answers don't appear.</p>
<p>It this does so, thanks <a href="http://help.openstreetmap.org/users/647/sk53"></a><a href="http://help.openstreetmap.org/users/647/sk53">@SK53</a>. Your answer was very clarifying.</p>
<p>I came across these question ( <a href="https://help.openstreetmap.org/questions/9343/drawing-and-addressing-apartment-complexes">https://help.openstreetmap.org/questions/9343/drawing-and-addressing-apartment-complexes</a> ) and this wiki entry ( <a href="http://wiki.openstreetmap.org/wiki/Key:addr:flats">http://wiki.openstreetmap.org/wiki/Key:addr:flats</a> ), which answer also my question.</p>
</div>
<div id="comment-36673-info" class="comment-info">
<span class="comment-age">(08 Sep '14, 04:36)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
</div>
<div id="comment-tools-36506" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-36506-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36497"></span>

<div id="answer-container-36497" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-36497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>H xoko, tag like Andy said and ad the address numbers like this, <a href="http://www.openstreetmap.org/#map=18/51.82707/4.97768">http://www.openstreetmap.org/#map=18/51.82707/4.97768</a> So youll have space for specific building tags as you described.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-36497" class="comments-container">
<span id="36513"></span>
<div id="comment-36513" class="comment">
<div id="post-36513-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems OK, is it bad practice.</p>
</div>
<div id="comment-36513-info" class="comment-info">
<span class="comment-age">(02 Sep '14, 15:46)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="36537"></span>
<div id="comment-36537" class="comment">
<div id="post-36537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not an OSM expert, but this doesn't sound very good practice. Anyway it's not what I was asking. I was asking how to tag different building with the same address but different apartment numbers, i.e, Building (A) -&gt; 123 Fake Street, contains apartments from 100 to 199. Building (B) -&gt; 123 Fake Street, contains apartments from 200 to 299.</p>
</div>
<div id="comment-36537-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 04:34)</span> <span class="comment-user userinfo">xoko</span>
</div>
</div>
<span id="36648"></span>
<div id="comment-36648" class="comment">
<div id="post-36648-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9575/xoko">@xoko</a> I think the addresses in the link are from an import of government data; they may be accurately located, but they are not very useful for actually finding the addresses &amp; routing to them.</p>
</div>
<div id="comment-36648-info" class="comment-info">
<span class="comment-age">(06 Sep '14, 08:04)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36497-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36496"></span>

<div id="answer-container-36496" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36496-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-36496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would draw building as a polygon, tag building=apartments. In Potlatch2 there a choice for that for buildings. in iD draw area, select building, select apartments. I couldn't find much advice beyond that in the wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '14, 15:42</strong> </span></p>
</div>
</div>
<div id="comments-container-36496" class="comments-container">
<span id="36505"></span>
<div id="comment-36505" class="comment">
<div id="post-36505-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The link to tourism=apartment is misleading. The OP is asking about blocks of residential flats/apartments, not tourist lettings.</p>
</div>
<div id="comment-36505-info" class="comment-info">
<span class="comment-age">(02 Sep '14, 14:03)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36566"></span>
<div id="comment-36566" class="comment">
<div id="post-36566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have deleted that misleading link</p>
</div>
<div id="comment-36566-info" class="comment-info">
<span class="comment-age">(03 Sep '14, 20:09)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-36496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36496-form-container" class="comment-form-container">
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

