+++
type = "question"
title = "Address information in POI *and* building?"
description = '''Hello everyone, I am getting into OSM mapping and have a question to the community concerning addresses. I know there is no standard for address mapping and several ways to do it (buildings, POIs or relations). I would like to have your take on my question: I am currently mapping in the US, where ma...'''
date = "2016-03-18T14:31:00Z"
lastmod = "2022-03-29T21:20:00Z"
weight = 48735
keywords = [ "buildings", "poi", "housenumbers", "address" ]
aliases = [ "/questions/48735" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Address information in POI \*and\* building?](/questions/48735/address-information-in-poi-and-building)

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
<span id="post-48735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48735-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-48735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I am getting into OSM mapping and have a question to the community concerning addresses. I know there is no standard for address mapping and several ways to do it (buildings, POIs or relations). I would like to have your take on my question:</p>
<p>I am currently mapping in the US, where many buildings already have addresses (partly from publicly available GIS data sets). This means that the building is a way mapped as building=yes and with various tags such as addr:street = F Street Northwest addr:housenumber = 2519 ...</p>
<p>Now if I add a POI to this building, for example a shop on the ground floor. Would you recommend adding the addr: <em>information (that is already contained in the building information) to the shop's POI? Yes or no?</em> Yes <em>would mean that the shop's POI information is as complete as possible, but that the address information is contained in the map twice: once in the building, once in the POI.</em> No* would mean that the shop's POI is in some regards incomplete, but it somehow seems cleaner to have no information repetition.</p>
<p>Cheers and Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '16, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/964d1a2453f009cfb7858fb7044449f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabon&#39;s gravatar image" />
<p><span>rabon</span><br />
<span class="score" title="221 reputation points">221</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48735" class="comments-container">
<span id="48993"></span>
<div id="comment-48993" class="comment">
<div id="post-48993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Similar question: <a href="/questions/47319/osmose-error-number-twice-in-the-street-when-adding-a-poi-with-house-number">https://help.openstreetmap.org/questions/47319/osmose-error-number-twice-in-the-street-when-adding-a-poi-with-house-number</a></p>
</div>
<div id="comment-48993-info" class="comment-info">
<span class="comment-age">(01 Apr '16, 10:58)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-48735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48735-form-container" class="comment-form-container">
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

<span id="48744"></span>

<div id="answer-container-48744" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48744-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-48744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rabon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We are dealing with a geographical database under the covers and all the data consumers should easily determine that a point (POI) within a polygon (building) shares the address of the polygon. So it is not necessary and many consider it potentially harmful as if something changes it is one more thing that needs to be maintained. The general philosophy is to enter something only once. And there are some QA tools that will definitely flag that as an error to be corrected, so don't be surprised if some remote mapper fixes that for you.</p>
<p>Another situation that comes up is a place with multiple buildings all sharing the same address. You can deal with that by drawing another polygon around the buildings and putting the address on that. No need for a relation here either, all the routing and mapping software deduce the buildings all have the address of the surrounding polygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '16, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-48744" class="comments-container">
<span id="48908"></span>
<div id="comment-48908" class="comment">
<div id="post-48908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with that as well as well as with the opposing point raised above by SK53 about ease-of-readibility. I realize that e.g. Osmose flags multiple addresses as erroneous entries. In the US, one building often hosts several addresses, which are then shown as their own nodes. That opens a third option, namely adding another node (a shop, for example) close to the address node, or adding the shop tags to the existing address node. I guess, for a good data reader this should make no difference, and I realize that there is no coherent practice for how to do this in OSM.</p>
</div>
<div id="comment-48908-info" class="comment-info">
<span class="comment-age">(29 Mar '16, 16:43)</span> <span class="comment-user userinfo">rabon</span>
</div>
</div>
<span id="48992"></span>
<div id="comment-48992" class="comment">
<div id="post-48992-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/12091/rabon">@rabon</a>: One building often with several addresses can be elegantly tagged by tagging the entrances, as usually each entrance is assigned one address. If not, you can tag a range (addr:housenumber=33-37). Some mappers also create separate address nodes, but I would not consider that a good idea. Address information should be attached to some object that "has" that address (be it an area, a building, or an entrance).</p>
</div>
<div id="comment-48992-info" class="comment-info">
<span class="comment-age">(01 Apr '16, 10:57)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="49017"></span>
<div id="comment-49017" class="comment">
<div id="post-49017-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/666/sleske">@sleske</a>: I think this is a great point. I am currently surveying and mapping in the Washington, DC, area. Most buildings, streets and addresses here come from public GIS data sets. Many of these tag the addresses in a single node on the building (which often comprises several addresses). I realy like the sound of your solution, and will consider it for future mapping. For now, the quasi-standard seems to be individual address nodes on buildings. Which, I agree with you, is not optimal.</p>
</div>
<div id="comment-49017-info" class="comment-info">
<span class="comment-age">(04 Apr '16, 04:13)</span> <span class="comment-user userinfo">rabon</span>
</div>
</div>
</div>
<div id="comment-tools-48744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48744-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48736"></span>

<div id="answer-container-48736" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48736-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-48736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see no problem with adding the address information to the POI as well.</p>
<p>The very nature of tags in OSM mean that we do duplicate information all over the place so trying to avoid it for notions of a clean dataset is probably self defeating. People who do want this type of clean dataset already have to implement suitable data cleansing processes on OSM data; and this should be good practise for any one using OSM as a source.</p>
<p>Furthermore a clean implementation of addresses would treat them as first class objects and not as attributes, so any OSM approach to addresses will <strong>never</strong> satisfy the requirements of a truly elegant approach (here just one example of a different issue, <a href="https://www.openstreetmap.org/relation/2164745#map=17/59.45200/24.73431">multiple buildings</a> all having the same address). However, rest assured we are not alone, almost every customer system in the world treats addresses as attributes.</p>
<p>Having to query buildings or parcels for associated address information does impose more complications for people consuming the information. So the duplication of data may assist people not interested in using the building data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '16, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-48736" class="comments-container">
<span id="48737"></span>
<div id="comment-48737" class="comment">
<div id="post-48737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your complete answer. I agree with you, it seems to make more sense to add as much information as possible rather than creating a beautiful dataset which then might fail if not read correctly. What is your take on using relations for this issue? Some (10% on average I have read in the osm wiki (?)) buildings use relations to connect information shared by POIs and the building or even several buildings such as the house number or the street. I presume adding a relation as a third way of storing address information (additionally to storing it in the POI and the building) is a possibility. But it also seems to be not too popular, partly because of relation's more complex nature compared to POI/building mapping. Would you agree? Cheers</p>
</div>
<div id="comment-48737-info" class="comment-info">
<span class="comment-age">(18 Mar '16, 16:02)</span> <span class="comment-user userinfo">rabon</span>
</div>
</div>
<span id="48738"></span>
<div id="comment-48738" class="comment">
<div id="post-48738-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>I also see no problem in adding address information twice, just the contrary. But I would rather refrain from using relations. My main reason for both is that we heavily rely on random users contributing to OSM. For those it should be made as easy as possible to add or correct information. While there are enough "specialists" out there heavily getting every detail into the complex railway and public transport relations it's those simple elements as shops and amenities that are still far from completely mapped and where we need the not so data-objects-savvy users for.</p>
</div>
<div id="comment-48738-info" class="comment-info">
<span class="comment-age">(18 Mar '16, 16:23)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="48742"></span>
<div id="comment-48742" class="comment">
<div id="post-48742-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> yes, very good point which I should have made.</p>
</div>
<div id="comment-48742-info" class="comment-info">
<span class="comment-age">(18 Mar '16, 19:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="48988"></span>
<div id="comment-48988" class="comment">
<div id="post-48988-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>While I agree with the "keep it simple" approach, there <em>is</em> a problem with redundant address tagging: It becomes harder to tell wether an address really exists multiple times, or is only stored redundantly. E.g., if I search for "33, Xstreet", which is a building containing multiple shops, I should only get one hit. However, if there really are two buildings with this address, I want two hits. This can be solved with filtering, but it's tricky.</p>
</div>
<div id="comment-48988-info" class="comment-info">
<span class="comment-age">(01 Apr '16, 09:26)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="84043"></span>
<div id="comment-84043" class="comment">
<div id="post-84043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/666/sleske">@sleske</a> you would have to distinguish whether the address information is just an attribute of something, or is a first class object on its own (possibly by using different tags)</p>
</div>
<div id="comment-84043-info" class="comment-info">
<span class="comment-age">(29 Mar '22, 21:20)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-48736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48736-form-container" class="comment-form-container">
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

