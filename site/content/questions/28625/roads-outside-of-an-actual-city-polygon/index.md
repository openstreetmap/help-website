+++
type = "question"
title = "Roads outside of an actual city polygon"
description = '''Hello, I have noticed that searching for an place that has an address outside of the actual city (admin boundary) will not show up in Nominatim. I know that you can add an addr:city tag to the road the place is located on to correct this. But that would mean that every single road outside of the cit...'''
date = "2013-11-30T18:59:00Z"
lastmod = "2013-12-19T14:55:00Z"
weight = 28625
keywords = [ "addressing" ]
aliases = [ "/questions/28625" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Roads outside of an actual city polygon](/questions/28625/roads-outside-of-an-actual-city-polygon)

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
<span id="post-28625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28625-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have noticed that searching for an place that has an address outside of the actual city (admin boundary) will not show up in Nominatim. I know that you can add an addr:city tag to the road the place is located on to correct this. But that would mean that every single road outside of the city would have to be tagged with addr:city for it to appear. Is there a way to automatically add that tag to every road outside of the city without having to add it to every single road?</p>
<p>For example, in the town of Glen Rock, PA (rural town) most of the roads are not in the actual polygon for the town. If you search for a road outside of Glen Rock by typing in Example Road glen rock pa, the road will not be found. With a lot of rural roads, adding addr:city to every road would be very time consuming. Is their any automatic tagging for such roads?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '13, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/b8f0abc33b0497474371dd84d9287786?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="auser1000&#39;s gravatar image" />
<p><span>auser1000</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="auser1000 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '13, 23:41</strong> </span></p>
</div>
</div>
<div id="comments-container-28625" class="comments-container">
<span id="28640"></span>
<div id="comment-28640" class="comment">
<div id="post-28640-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think there's any automatic tagging, no, in part because there's no deterministic way to know what "town name" to attach the road to. I asked a related question a while back ( <a href="https://help.openstreetmap.org/questions/19407/how-to-make-post-office-town-available-to-nominatim">https://help.openstreetmap.org/questions/19407/how-to-make-post-office-town-available-to-nominatim</a> ) and the only answer I got was to manually add addr:city tags....</p>
</div>
<div id="comment-28640-info" class="comment-info">
<span class="comment-age">(01 Dec '13, 08:51)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
<span id="29146"></span>
<div id="comment-29146" class="comment">
<div id="post-29146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well, if you read the comments to the answer on the question you cite, two people said <em>not</em> to tag addr:city, which is as many as voted the answer up. that is, it doesn't seem like an answer with real consensus. you might take another look at Twain's answer there, as Twain is one of the maintainers of Nominatim.</p>
</div>
<div id="comment-29146-info" class="comment-info">
<span class="comment-age">(17 Dec '13, 17:38)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="29168"></span>
<div id="comment-29168" class="comment">
<div id="post-29168-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree that there's no consensus here on what to do, although I'll also point out that one of the "don't tag addr:city" comments was only posted after I linked it from here. In any case, mostly I'd just like to find out how to solve the problem; I don't really have a preferred solution as long as something works.</p>
</div>
<div id="comment-29168-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 16:08)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-28625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28625-form-container" class="comment-form-container">
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

<span id="28664"></span>

<div id="answer-container-28664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not add addr:city to roads at all. The addr:* tags are meant for objects that have an address. Roads don't.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '13, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-28664" class="comments-container">
<span id="28670"></span>
<div id="comment-28670" class="comment">
<div id="post-28670-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This directly contradicts the advice given on my question ( <a href="https://help.openstreetmap.org/questions/19407/how-to-make-post-office-town-available-to-nominatim">https://help.openstreetmap.org/questions/19407/how-to-make-post-office-town-available-to-nominatim</a> ), where moreover one of the comments says that addr:city is <em>only</em> relevant on streets, not addressable nodes.</p>
</div>
<div id="comment-28670-info" class="comment-info">
<span class="comment-age">(01 Dec '13, 20:45)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-28664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28645"></span>

<div id="answer-container-28645" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question corresponds IMHO to the following single problems:</p>
<ol>
<li><p><strong>Wrong place association in Nominatim</strong><br />
As you already described, geocoding from OSM data relies on a 2 step preprocessing to normalize the data. First they filter all address objects and then they try to expand them to full 'global addresses' using hierarchies (boundary polygones or surrounding areas around place nodes).<br />
This process is fragile, as polygones can be broken or have a unexpected classification, or can have wrong (here: not the official) geometry.<br />
I was sadly unable to find your example, but if the road doesn't touch the official town border, then the border of the town might just be wrong?<br />
On the other hand, you might use <strong>nominatims "near" operator</strong> to find a road that is close to a spec. city like "my road near Glen Rock, PA".</p></li>
<li><p><strong>use addr: tag fixes:</strong><br />
Corresponding to the wiki, the addr: key is only used for buildings or POIs?<br />
<a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a><br />
<a href="http://wiki.openstreetmap.org/wiki/Karlsruhe_Schema">http://wiki.openstreetmap.org/wiki/Karlsruhe_Schema</a><br />
<a href="http://wiki.openstreetmap.org/wiki/Addresses">http://wiki.openstreetmap.org/wiki/Addresses</a><br />
I only know <a href="http://wiki.openstreetmap.org/wiki/Key:postal_code">postal_code=*</a> that is tagged to the streets directly. So for me this sounds a bit like <a href="http://wiki.openstreetmap.org/wiki/Best_practices#Don.27t_map_for_the_renderer">'tagging for renderer'</a> (here: geocoder) to fix specific misbehavior of a product and that should avoided. So we need to discuss to find the technical reasons and <a href="http://wiki.openstreetmap.org/wiki/Automated_Edits">avoid mechanical edits</a>. Please hop in the forums or the mailinglists :)</p></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '13, 10:36</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-28645" class="comments-container">
<span id="28669"></span>
<div id="comment-28669" class="comment">
<div id="post-28669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your answer presumes that all roads associated with a town are within the borders of that town, which may be true in some jurisdictions but is emphatically <em>not</em> true in much of the US (and Ireland, apparently). This is not a question of tagging for the renderer. See my other question ( <a href="https://help.openstreetmap.org/questions/19407/how-to-make-post-office-town-available-to-nominatim">https://help.openstreetmap.org/questions/19407/how-to-make-post-office-town-available-to-nominatim</a> ) for more details of the situation. The specific advice there was to use addr:city on the streets.</p>
</div>
<div id="comment-28669-info" class="comment-info">
<span class="comment-age">(01 Dec '13, 20:43)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-28645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28645-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29163"></span>

<div id="answer-container-29163" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29163-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are <strong>confusing administrative entities and settlements</strong>.</p>
<p>You can have a place-polygon (or multipolygon) for the settlement and another one for the administrative entity.</p>
<p>It is not unusual that the two are not the same. Personally I'd use the place polygon on the built-up space belonging (according to who lives there) to the settlement, while the administrative entities (boundary=administrative, admin_level=x) are those as authoritively defined.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Dec '13, 12:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29163" class="comments-container">
<span id="29169"></span>
<div id="comment-29169" class="comment">
<div id="post-29169-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not sure that's actually the problem here; it's more that there are two different administrative entities. The named built-up space (to which you would assign the place polygon) may correspond to either, both, or neither of the main administrative entities. To use an example close to where I live, there <em>are</em> people who are outside the official town limits of Farmville but generally say they live "in Farmville"; but there are also people who live well outside of town but whose mailing address (and address to look up on maps) is "in" Farmville.</p>
</div>
<div id="comment-29169-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 16:19)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
<span id="29174"></span>
<div id="comment-29174" class="comment">
<div id="post-29174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well, I agree that mailing addresses are yet another system / class, not necessarily covered by administrative entities and geographic settlements (i.e. boundary=administrative and place=*). The right way to tag them is addr:* (but it isn't the streets that have the address, but it's people or businesses which happen to be along this street).</p>
</div>
<div id="comment-29174-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 20:40)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="29199"></span>
<div id="comment-29199" class="comment">
<div id="post-29199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>blahedo, I don't think there are two different <em>administrative</em> entities. There is one: the municipality and its boundary. The second thing you're referring to is the postal address, which is based on what the postal service determines is the zip code and preferred mailing city for that address. You're talking about ways to add that data to OSM, but it doesn't really fit very well. That's one reason why Nominatim uses some non-OSM data. The place=* (settlement) tags sometimes are coincident to the admin tags, but sometimes offer an alternative to them.</p>
</div>
<div id="comment-29199-info" class="comment-info">
<span class="comment-age">(19 Dec '13, 14:55)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-29163" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29163-form-container" class="comment-form-container">
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

