+++
type = "question"
title = "Accessing openstreet map on ubuntu server from centos web server"
description = '''I have setup an ubuntu server based on the switch2osm steps. So now I have downloaded the latest openlayer scripts and below is my script. &amp;lt;script&amp;gt;  var map = new ol.Map({  layers: [  new ol.layer.Tile({  source: new ol.source.OSM({  url: &#x27;http://mapserverIP/osm_tiles/{z}/{x}/{y}.png&#x27;  })  }) ...'''
date = "2017-07-16T18:09:00Z"
lastmod = "2017-07-16T18:09:00Z"
weight = 57121
keywords = [ "centos", "ubuntu" ]
aliases = [ "/questions/57121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Accessing openstreet map on ubuntu server from centos web server](/questions/57121/accessing-openstreet-map-on-ubuntu-server-from-centos-web-server)

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
<span id="post-57121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57121-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup an ubuntu server based on the switch2osm steps. So now I have downloaded the latest openlayer scripts and below is my script.</p>
<pre><code>&lt;script&gt;
    var map = new ol.Map({
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM({
             url: &#39;http://mapserverIP/osm_tiles/{z}/{x}/{y}.png&#39;
          })
       })
     ],
     target: &#39;map&#39;,
     controls: ol.control.defaults({
        attributionOptions: /** @type {olx.control.AttributionOptions} */ ({
          collapsible: false
        })
     }),
    view: new ol.View({
       center: [244780.24508882355, 7386452.183179816],
       zoom:5
    })
 });</code></pre>
<p>I get the following errors. Access to Image at 'http://mapserverIP/osm_tiles/5/16/10.png' from origin 'http://webserIP' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://webserIP' is therefore not allowed access. The response had HTTP status code 404.</p>
<p>Then I added this</p>
<pre><code>   source: new ol.source.OSM({
             url: &#39;http://mapserverIP/osm_tiles/{z}/{x}/{y}.png&#39;,
            crossOrigin: null
          })
       })</code></pre>
<p>the above error is gone but now I get this error <code>GET </code><a href="http://mapserverIP/osm_tiles/5/16/10.png"><code>http://mapserverIP/osm_tiles/5/16/10.png</code></a><code> 404 (Not Found)</code> I have added this now view: new ol.View({ center: ol.proj.transform([4.258768357307995, 101.832275390625], 'EPSG:4326', 'EPSG:3857'), zoom:5 }) There is no error but the map is empty white color ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-centos" rel="tag" title="see questions tagged &#39;centos&#39;">centos</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '17, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '17, 18:24</strong> </span></p>
</div>
</div>
<div id="comments-container-57121" class="comments-container">
&#10;</div>
<div id="comment-tools-57121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57121-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

