+++
type = "question"
title = "OSM geocoding inverse :local wamp"
description = '''I am using the following code to retrieve the address from lon and lat:  $lon = 100.753;  $lat = 13.69362; function getAddress($RG_Lat,$RG_Lon) {  $json = &quot;https://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat=&quot;.$RG_Lat.&quot;&amp;amp;lon=&quot;.$RG_Lon.&quot;&amp;amp;zoom=27&amp;amp;addressdetails=1&quot;;   $ch = curl_...'''
date = "2021-05-23T23:12:00Z"
lastmod = "2021-05-26T18:00:00Z"
weight = 80268
keywords = [ "geocoding" ]
aliases = [ "/questions/80268" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSM geocoding inverse :local wamp](/questions/80268/osm-geocoding-inverse-local-wamp)

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
<span id="post-80268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80268-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using the following code to retrieve the address from lon and lat: $lon = 100.753; $lat = 13.69362;</p>
<pre><code>function getAddress($RG_Lat,$RG_Lon)
{
  $json = &quot;https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=&quot;.$RG_Lat.&quot;&amp;lon=&quot;.$RG_Lon.&quot;&amp;zoom=27&amp;addressdetails=1&quot;;
&#10;  $ch = curl_init($json);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_USERAGENT, &quot;Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0&quot;);
  $jsonfile = curl_exec($ch);
  curl_close($ch);
&#10;  $RG_array = json_decode($jsonfile,true);
&#10;  return $RG_array[&#39;display_name&#39;];
  // $RG_array[&#39;address&#39;][&#39;city&#39;];
  // $RG_array[&#39;address&#39;][&#39;country&#39;];
}
&#10;$addr = getAddress($lat,$lon);
echo &quot;Address: &quot;.$addr;</code></pre>
<p>My code works very well under ovh server.</p>
<p>My application is installed locally under wamp server.</p>
<p>The same code, does not return anything: What extension or something else that I must activate it locally to have a return of my code?</p>
<p>Do you have any idea, why my code no longer works locally (wamp server)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '21, 23:12</strong></p>
<img src="https://secure.gravatar.com/avatar/bb762f011c30332a088e644823f52ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lemjid&#39;s gravatar image" />
<p><span>Lemjid</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lemjid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '21, 08:46</strong> </span></p>
</div>
</div>
<div id="comments-container-80268" class="comments-container">
<span id="80289"></span>
<div id="comment-80289" class="comment">
<div id="post-80289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello everyone, Someone has an approach, an idea: is it possible to use this code locally as my application is well installed locally ???</p>
</div>
<div id="comment-80289-info" class="comment-info">
<span class="comment-age">(25 May '21, 16:13)</span> <span class="comment-user userinfo">Lemjid</span>
</div>
</div>
<span id="80293"></span>
<div id="comment-80293" class="comment">
<div id="post-80293-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Help please ????????</p>
</div>
<div id="comment-80293-info" class="comment-info">
<span class="comment-age">(25 May '21, 18:39)</span> <span class="comment-user userinfo">Lemjid</span>
</div>
</div>
<span id="80306"></span>
<div id="comment-80306" class="comment">
<div id="post-80306-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You probably aren't getting any responses because nobody here knows how to help you. This doesn't sound like an OSM issue, but rather a more general issue with configuring a web server. You might get more help from somewhere like StackOverflow.</p>
</div>
<div id="comment-80306-info" class="comment-info">
<span class="comment-age">(26 May '21, 17:35)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="80307"></span>
<div id="comment-80307" class="comment">
<div id="post-80307-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@Alester</a> : thanks</p>
</div>
<div id="comment-80307-info" class="comment-info">
<span class="comment-age">(26 May '21, 17:57)</span> <span class="comment-user userinfo">Lemjid</span>
</div>
</div>
<span id="80308"></span>
<div id="comment-80308" class="comment">
<div id="post-80308-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To add to what alester said - if something works in place A but not in place B then the difference is between place A and place B, and we don't have any information about those and so can't really comment.</p>
</div>
<div id="comment-80308-info" class="comment-info">
<span class="comment-age">(26 May '21, 18:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80268-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

