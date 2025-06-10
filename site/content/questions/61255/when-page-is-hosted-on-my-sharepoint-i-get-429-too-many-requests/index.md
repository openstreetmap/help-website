+++
type = "question"
title = "When page is hosted on my sharepoint, I get 429 Too many requests"
description = '''I have a leaflet map on a html page I use to show certain geopositioned assets from my database.  One of the features uses nominatim reverse query for certain user actions. The actions that end in nominatim query are less than one per second, even less than one per minute. It works perfectly when ru...'''
date = "2017-12-18T10:19:00Z"
lastmod = "2018-01-03T11:58:00Z"
weight = 61255
keywords = [ "nominatim", "sharepoint" ]
aliases = [ "/questions/61255" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [When page is hosted on my sharepoint, I get 429 Too many requests](/questions/61255/when-page-is-hosted-on-my-sharepoint-i-get-429-too-many-requests)

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
<span id="post-61255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61255-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a leaflet map on a html page I use to show certain geopositioned assets from my database.</p>
<p>One of the features uses nominatim reverse query for certain user actions. The actions that end in nominatim query are less than one per second, even less than one per minute.</p>
<p>It works perfectly when run on my localhost, and when run from a test server. But when I put my page on my sharepoint server all the nominatim queries end with a 429 Too Many Requests response.</p>
<p>The requests come from jQuery code executed on the browser, either firefox or chrome.</p>
<p>For simplifying and making the point, let's say that the code is run in a click handler of the map</p>
<pre><code>  map.on(&#39;click&#39;, e=&gt; {
    let popup = L.popup();
    popup
      .setLatLng(e.latlng)
      .setContent(`[${e.latlng.lat.toFixed(5)},${e.latlng.lng.toFixed(5)}]`)
      .openOn(map);
    reverseGeocode(e.latlng, res =&gt; {
      popup.setContent(`[${e.latlng.lat.toFixed(5)},${e.latlng.lng.toFixed(5)}]&lt;br&gt;${res.display_name}`);
     });
});</code></pre>
<p>and the reverse geocoding function just invokes the url with a jsonp wrap</p>
<pre><code>function reverseGeocode(latlng,callback) {
    let url=`https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=${latlng.lat}&amp;lon=${latlng.lng}`;
    $.ajax({ url, 
      dataType:&quot;jsonp&quot;,
      jsonp: &quot;json_callback&quot;,
      success: callback
    });
  }
};</code></pre>
<p>This code is in the page, and the page is in a private document library in my private sharepoint site hosted by microsoft office365 and accessed as xxxxxx.sharepoint.com</p>
<p>What can I do to solve this limitation?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-sharepoint" rel="tag" title="see questions tagged &#39;sharepoint&#39;">sharepoint</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '17, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/a413c9b950c3c2558d572bfd2bcb1d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="P%20A&#39;s gravatar image" />
<p><span>P A</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="P A has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Dec '17, 12:23</strong> </span></p>
</div>
</div>
<div id="comments-container-61255" class="comments-container">
<span id="61257"></span>
<div id="comment-61257" class="comment">
<div id="post-61257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the Nominatim queries always originate from the user and not from the server?</p>
</div>
<div id="comment-61257-info" class="comment-info">
<span class="comment-age">(18 Dec '17, 11:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="61258"></span>
<div id="comment-61258" class="comment">
<div id="post-61258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have updated my question with more information on the code</p>
</div>
<div id="comment-61258-info" class="comment-info">
<span class="comment-age">(18 Dec '17, 12:23)</span> <span class="comment-user userinfo">P A</span>
</div>
</div>
</div>
<div id="comment-tools-61255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61255-form-container" class="comment-form-container">
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

<span id="61460"></span>

<div id="answer-container-61460" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61460-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In contrast to Firefox and Chrome, your sharepoint server likely does not send a HTTP referrer or user agent as requested by <a href="https://operations.osmfoundation.org/policies/nominatim/">Nominatim's usage policy</a>. You will need to consult the sharepoint documentation and/or contact your hoster to find out how to change that. Once a proper referrer/user agent is set, the error will go away.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '18, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-61460" class="comments-container">
&#10;</div>
<div id="comment-tools-61460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61460-form-container" class="comment-form-container">
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

