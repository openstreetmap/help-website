+++
type = "question"
title = "reverse geocoding doesn&#x27;t return postal code in Netherlands"
description = '''I was trying to use reverse Geocoding to retrieve postal code from give Lat Lon information. We are using it in a test case to validate some of our data. For germany it works fine, but if i try to use this same service for with Lat/Long from the Netherlands, the response does not contain postal code...'''
date = "2011-04-01T14:43:00Z"
lastmod = "2012-11-06T20:26:00Z"
weight = 4244
keywords = [ "netherlands", "postal", "code", "geocoding", "reverse" ]
aliases = [ "/questions/4244" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [reverse geocoding doesn't return postal code in Netherlands](/questions/4244/reverse-geocoding-doesnt-return-postal-code-in-netherlands)

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
<span id="post-4244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4244-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was trying to use reverse Geocoding to retrieve postal code from give Lat Lon information. We are using it in a test case to validate some of our data.</p>
<p>For germany it works fine, but if i try to use this same service for with Lat/Long from the Netherlands, the response does not contain postal code information.</p>
<p>do you know why this is? If i can remember correctly a while ago, it was using a different URL for the request, but it returned the postal code as a part of the response?</p>
<p>Sorry if it wasn't complete. here are two examples, both from center of different cities:</p>
<p><strong>Germany - Bochum:</strong></p>
<p><em>request</em> - <a href="https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=51.486514&amp;lon=7.20764"></a><a href="https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=51.486514&amp;lon=7.20764"></a><a href="https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=51.486514&amp;lon=7.20764">https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=51.486514&amp;lon=7.20764</a></p>
<p><em>response</em> - Präsidentstraße, Hamme, Bochum, Regierungsbezirk Arnsberg, North Rhine-Westphalia, 44789, Germany</p>
<p><strong>Netherlands - Utrecht:</strong></p>
<p><em>request</em> - <a href="https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=52.09914&amp;lon=5.123649"></a><a href="https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=52.09914&amp;lon=5.123649"></a><a href="https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=52.09914&amp;lon=5.123649">https://www.openstreetmap.org/geocoder/description_osm_nominatim?lat=52.09914&amp;lon=5.123649</a></p>
<p><em>response</em> - Jan van der Heijdenstraat, Utrecht, Bestuur Regio Utrecht, Utrecht, The Netherlands</p>
<p>The response from Netherlands, does not contain the postal code information.</p>
<p>The same results are obtained if you use the following URL:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?lat=52.09914&amp;lon=5.123649"></a><a href="http://nominatim.openstreetmap.org/reverse?lat=52.09914&amp;lon=5.123649"></a><a href="http://nominatim.openstreetmap.org/reverse?lat=52.09914&amp;lon=5.123649">http://nominatim.openstreetmap.org/reverse?lat=52.09914&amp;lon=5.123649</a></p>
<p>Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-netherlands" rel="tag" title="see questions tagged &#39;netherlands&#39;">netherlands</span> <span class="post-tag tag-link-postal" rel="tag" title="see questions tagged &#39;postal&#39;">postal</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '11, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/11536e2e01a1ea7cc3840b994f9d27e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pance&#39;s gravatar image" />
<p><span>pance</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pance has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Apr '11, 15:49</strong> </span></p>
</div>
</div>
<div id="comments-container-4244" class="comments-container">
<span id="4245"></span>
<div id="comment-4245" class="comment">
<div id="post-4245-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you edit your question and add some more information, especially one URL from Germany where it works, one URL from Netherlands where it fails, and: what engine/web-app are you using for geocoding?</p>
</div>
<div id="comment-4245-info" class="comment-info">
<span class="comment-age">(01 Apr '11, 15:29)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="4270"></span>
<div id="comment-4270" class="comment">
<div id="post-4270-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe related, I've noticed that the street/postcodes in the Netherlands are not connected to the city. So for instance, looking for "Mendelssohnstraat, Delft" doesn't lead to any result, while it should return: <a href="http://open.mapquestapi.com/nominatim/v1/details.php?place_id=15301180">http://open.mapquestapi.com/nominatim/v1/details.php?place_id=15301180</a> (Mendelssohnstraat, 2625 AD, The Netherlands)</p>
<p>Not sure whether it's a problem in the data or Nominatim.</p>
</div>
<div id="comment-4270-info" class="comment-info">
<span class="comment-age">(04 Apr '11, 16:19)</span> <span class="comment-user userinfo">Éric Piel</span>
</div>
</div>
</div>
<div id="comment-tools-4244" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4244-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="4254"></span>

<div id="answer-container-4254" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4254-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>Disclaimer: I'm no expert on Nominatim</em></p>
<p>The reason your query for Utrecht does not return a postcode is apparently quite simply that the OSM database does not contain postcode information for the street. As with any other information, OSM only contains what users have entered, and for some areas (notably house numbers and postcodes) coverage is often very spotty, even in regions where streets and street names are fairly complete.</p>
<p>If you search for other streets in the Netherlands using Nominatim, you'll see that you sometimes get postcode information, and sometimes not. For example,</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?lat=52.65285&amp;lon=6.03195">http://nominatim.openstreetmap.org/reverse?lat=52.65285&amp;lon=6.03195</a></p>
<p>will give you postcode information.</p>
<p>That said, even if you do get a postcode, you cannot necessarily rely on it in all areas. Notably, your example result for "Präsidentenstraße, Bochum" is wrong - the correct postcode is 44791, and not 44789, as Nominatim reports (check it on e.g. <a href="http://www.postleitzahl.de/">http://www.postleitzahl.de/</a> ).</p>
<p>So, in order to use postcode information from Nominatim, you'd first need to check whether there is reliable postcode information for the region of interest. If there is, the calls you used should return the postcode. If they don't, then that's another question...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '11, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-4254" class="comments-container">
<span id="4271"></span>
<div id="comment-4271" class="comment">
<div id="post-4271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer sleske.</p>
<p>I am aware that the information is not always 100% correct. It can be edited all the time, but this is not relevant at this point.</p>
<p><em>"The reason your query for Utrecht does not return a postcode is apparently quite simply that the OSM database does not contain postcode information for the street.</em>"</p>
<p>The reason i raised this thread is that i am pretty sure that this information existed. Then simply some weeks ago it was not returned any more as part of the response.</p>
<p>My concern was as to why was this, and if anyone was aware of it? Was there maybe some law that forbids displaying postal code details in reverse geocoding? or etc.</p>
</div>
<div id="comment-4271-info" class="comment-info">
<span class="comment-age">(04 Apr '11, 16:33)</span> <span class="comment-user userinfo">pance</span>
</div>
</div>
<span id="17527"></span>
<div id="comment-17527" class="comment">
<div id="post-17527-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe it's license change related scrubbing?</p>
</div>
<div id="comment-17527-info" class="comment-info">
<span class="comment-age">(06 Nov '12, 20:26)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-4254" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4254-form-container" class="comment-form-container">
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

