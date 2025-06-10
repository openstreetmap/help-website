+++
type = "question"
title = "How to set my country to be default location when openning openlayer"
description = '''Hello,  I am refering this site http://openlayers.org/en/latest/examples/localized-openstreetmap.html and its working fine with my internal tiles only for one country.  I would like to understand  when i will type http://192.168.1.32/index.html , how Can I make my country to be default on the screen...'''
date = "2018-05-25T10:03:00Z"
lastmod = "2018-05-26T11:27:00Z"
weight = 63731
keywords = [ "openstreetmap", "openlayers" ]
aliases = [ "/questions/63731" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to set my country to be default location when openning openlayer](/questions/63731/how-to-set-my-country-to-be-default-location-when-openning-openlayer)

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
<span id="post-63731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63731-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am refering this site <a href="http://openlayers.org/en/latest/examples/localized-openstreetmap.html">http://openlayers.org/en/latest/examples/localized-openstreetmap.html</a> and its working fine with my internal tiles only for one country. I would like to understand</p>
<p>when i will type <a href="http://192.168.1.32/index.html">http://192.168.1.32/index.html</a> , how Can I make my country to be default on the screen ? I tryed to use this " center: [23.75936, 90.37787]," but dont think thats the right place .</p>
<p>Bellow are the changed Code var openSeaMapLayer = new ol.layer.Tile({ source: new ol.source.OSM({ attributions: [ 'All maps © <a href="http://www.openseamap.org/">OpenSeaMap</a>', ol.source.OSM.ATTRIBUTION ], opaque: false, url: 'http://192.168.1.32/hot/{z}/{x}/{y}.png' }) });</p>
<pre><code>  var map = new ol.Map({
    layers: [
      openCycleMapLayer,
      openSeaMapLayer
    ],
    target: &#39;map&#39;,
    controls: ol.control.defaults({
      attributionOptions: {
        collapsible: false
      }
    }),
    view: new ol.View({
      maxZoom: 25,
      center: [23.75936, 90.37787],
      zoom: 9
    })
  });</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 May '18, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '18, 10:26</strong> </span></p>
</div>
</div>
<div id="comments-container-63731" class="comments-container">
&#10;</div>
<div id="comment-tools-63731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63731-form-container" class="comment-form-container">
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

<span id="63735"></span>

<div id="answer-container-63735" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63735-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fosiul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello fosiul,</p>
<p>By default, OpenLayers uses Web Mercator Projection (<a href="http://epsg.io/3857">EPSG:3857</a>). So you cannot use Longitude, Latitude directly to set the center.</p>
<p>This is what you should use :</p>
<pre><code>view: new ol.View({
  maxZoom: 25,
  center: ol.proj.fromLonLat([90.37787,23.75936]),
  zoom: 9
})</code></pre>
<p>More documentation on ol.proj : <a href="http://openlayers.org/en/latest/apidoc/ol.proj.html">http://openlayers.org/en/latest/apidoc/ol.proj.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '18, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/08e299a7143fc92767e9c66bff9481bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbelien&#39;s gravatar image" />
<p><span>jbelien</span><br />
<span class="score" title="146 reputation points">146</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbelien has one accepted answer">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 May '18, 11:28</strong> </span></p>
</div>
</div>
<div id="comments-container-63735" class="comments-container">
<span id="63736"></span>
<div id="comment-63736" class="comment">
<div id="post-63736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Jbelien, Thanks for the References, i will read thsoe in details now, however for this I have changed this bellow, but when i open the browser its all blue then iw ill neeed to move to right place to get the county.</p>
<p>view: new ol.View({ maxZoom: 25, center: ol.proj.toLonLat([23.7593572,90.3788136]), zoom: 9</p>
<p>the reference county lat/lon is here</p>
<p><a href="https://www.openstreetmap.org/node/3442474911">https://www.openstreetmap.org/node/3442474911</a> I will also upload a picture to show what i get when i open the browser Thanks</p>
</div>
<div id="comment-63736-info" class="comment-info">
<span class="comment-age">(25 May '18, 14:25)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63737"></span>
<div id="comment-63737" class="comment">
<div id="post-63737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>picture attached in this link <a href="https://ibb.co/hLwa38">https://ibb.co/hLwa38</a></p>
<p>but if i zoom in/out right side then i can see the country</p>
</div>
<div id="comment-63737-info" class="comment-info">
<span class="comment-age">(25 May '18, 14:27)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63738"></span>
<div id="comment-63738" class="comment not_top_scorer">
<div id="post-63738-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you switched Latitude and Longitude.<br />
Parameter for <code>ol.proj.toLonLat</code> is Longitude, Latitude and not Latitude, Longitude !</p>
<pre><code>view: new ol.View({
  maxZoom: 25,
  center: ol.proj.toLonLat([90.37787, 23.75936]),
  zoom: 9
})</code></pre>
</div>
<div id="comment-63738-info" class="comment-info">
<span class="comment-age">(25 May '18, 14:28)</span> <span class="comment-user userinfo">jbelien</span>
</div>
</div>
<span id="63745"></span>
<div id="comment-63745" class="comment not_top_scorer">
<div id="post-63745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Jbelien, Sorry missed your post, i actually tryed this , but by putting zoom:4 , i see map but not the right one default, see the screen shot at <a href="https://ibb.co/h0dbd8">https://ibb.co/h0dbd8</a></p>
<p>view: new ol.View({ maxZoom: 18, center: ol.proj.toLonLat([90.527,23.918]), zoom: 4 })</p>
<p>its actually slightly off the page , if i drag the mouse bit right then i see the map : <a href="https://ibb.co/cqoHJ8,">https://ibb.co/cqoHJ8,</a> but i need to make this map in the front page Thanks for the help.</p>
</div>
<div id="comment-63745-info" class="comment-info">
<span class="comment-age">(25 May '18, 21:44)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63748"></span>
<div id="comment-63748" class="comment not_top_scorer">
<div id="post-63748-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like it's centering on 0,0 instead of your desired coordinates, so there must be something not quite right somewhere.</p>
</div>
<div id="comment-63748-info" class="comment-info">
<span class="comment-age">(26 May '18, 00:13)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="63750"></span>
<div id="comment-63750" class="comment not_top_scorer">
<div id="post-63750-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@Alester</a>, Thanks I am using this example <a href="http://openlayers.org/en/latest/examples/localized-openstreetmap.html">http://openlayers.org/en/latest/examples/localized-openstreetmap.html</a></p>
<p>any idea.. where could be the problem ?</p>
<p>Thanks</p>
</div>
<div id="comment-63750-info" class="comment-info">
<span class="comment-age">(26 May '18, 01:07)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63753"></span>
<div id="comment-63753" class="comment">
<div id="post-63753-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Shouldn't that be fromLonLat, not toLonLat? After all, you want to go <em>from</em> a lon/lat pair to projected coordinates.</p>
</div>
<div id="comment-63753-info" class="comment-info">
<span class="comment-age">(26 May '18, 09:12)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="63754"></span>
<div id="comment-63754" class="comment">
<div id="post-63754-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/3893/turepalsson">@Turepalsson</a>,</p>
<p>Thanks thats worked,</p>
<p>center: ol.proj.fromLonLat([90.413242,23.809595]),</p>
<p>Thanks for the help.</p>
</div>
<div id="comment-63754-info" class="comment-info">
<span class="comment-age">(26 May '18, 10:21)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63756"></span>
<div id="comment-63756" class="comment">
<div id="post-63756-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh yes, stupid me ...</p>
<p>Of course it's fromLonLat() ... Sorry for the confusion !</p>
<p>I fixed the code of my "solution" :)</p>
</div>
<div id="comment-63756-info" class="comment-info">
<span class="comment-age">(26 May '18, 11:27)</span> <span class="comment-user userinfo">jbelien</span>
</div>
</div>
</div>
<div id="comment-tools-63735" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63735-form-container" class="comment-form-container">
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

