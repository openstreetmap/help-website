+++
type = "question"
title = "General Overpass Servor Error"
description = '''I&#x27;m working on a project that downloads data from openstreetmap with R-Studio.  Fehler in check_for_error(doc) : General overpass server error; returned: The data included in this document is from www.openstreetmap.org. The data is made available under ODbL. runtime error: Query timed out in &quot;query&quot;...'''
date = "2021-04-16T16:24:00Z"
lastmod = "2021-04-17T16:33:00Z"
weight = 79685
keywords = [ "openstreetmap", "overpass", "error", "server" ]
aliases = [ "/questions/79685" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [General Overpass Servor Error](/questions/79685/general-overpass-servor-error)

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
<span id="post-79685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79685-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on a project that downloads data from openstreetmap with R-Studio.</p>
<p>Fehler in check_for_error(doc) : General overpass server error; returned: The data included in this document is from www.openstreetmap.org. The data is made available under ODbL. runtime error: Query timed out in "query" at line 5 after 26 seconds.</p>
<p>But every time I try to download data, I get this Error-code. Could you explain to me, what it means and how I could fix the problem. I would really appreciative, if you could help me.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Apr '21, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/950b64fca0edc74f18b586c909247976?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael23&#39;s gravatar image" />
<p><span>Michael23</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael23 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79685" class="comments-container">
<span id="79689"></span>
<div id="comment-79689" class="comment">
<div id="post-79689-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your query could ask for too many data. Why don't you post the relevant bit of code with the query?</p>
</div>
<div id="comment-79689-info" class="comment-info">
<span class="comment-age">(17 Apr '21, 10:15)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="79696"></span>
<div id="comment-79696" class="comment">
<div id="post-79696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the answer section you can find my script. It would really help me out, if you could help me to find the problem.</p>
</div>
<div id="comment-79696-info" class="comment-info">
<span class="comment-age">(17 Apr '21, 14:15)</span> <span class="comment-user userinfo">Michael23</span>
</div>
</div>
</div>
<div id="comment-tools-79685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79685-form-container" class="comment-form-container">
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

<span id="79695"></span>

<div id="answer-container-79695" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79695-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is the script as far as it goes, until I receive the error-code. If you could make out the problem, that would be really helpful.</p>
<pre><code>library(osmdata)
library(sf)
library(sp)
library(rgdal)
&#10;# Reading Data 
LostLetterFairtrade0221&lt;-readRDS(&quot;~/Documents/Forschungsseminar/LostLetterFairtrade0221.rds&quot;)
&#10;# Funktion to Convert from wgs84 to UTM
WGS.to.UTM&lt;-function(long, lat, utm.zone){
  utm.zone=as.character(utm.zone)
  if(length(utm.zone)==1){utm.zone=rep(utm.zone, length(long))}
  coords=data.frame(long, lat)
  names(coords)=c(&quot;long&quot;,&quot;lat&quot;)
  #prepare map for conversion to UTM:
  coordinates(coords)&lt;-c(&quot;long&quot;,&quot;lat&quot;)
  coords@proj4string=CRS(&quot;+proj=longlat +datum=WGS84&quot;)
  #deterine parameters of the transformation:
  #browser()
  transf.param=unlist(lapply(utm.zone, function(x){
    CRS(paste(&quot;+proj=utm +zone=&quot;, x ,&quot; +datum=WGS84&quot;, sep=&quot;&quot;))
  }))
  #... and transform it to UTM
  new.coords=lapply(1:length(coords), function(x){
    spTransform(coords[x,], transf.param[[x]])@coords
  })
  new.coords=as.data.frame(matrix(unlist(new.coords), ncol=2, byrow=T))
  names(new.coords)=c(&quot;long&quot;, &quot;lat&quot;)
  #new.coords$lat[new.coords$lat&lt;0]=10000000-new.coords$lat[new.coords$lat&lt;0]
  return(new.coords)
}
&#10;#### UTM-Koordinaten for the letters
utm33n_llocs=WGS.to.UTM(long=LostLetterFairtrade0221$long, lat=LostLetterFairtrade0221$lat, utm.zone=&quot;33N&quot;)
&#10;LostLetterFairtrade0221$long_utm33n=utm33n_llocs$long
LostLetterFairtrade0221$lat_utm33n=utm33n_llocs$lat
&#10;api_list &lt;- c(&#39;https://overpass.kumi.systems/api/interpreter&#39;)
api_to_use &lt;- sample(1:length(api_list), 1)
&#10;set_overpass_url(api_list[api_to_use])
&#10;#### Waldflächen ziehen
forest &lt;- opq(bbox = &quot;bb&quot;) %&gt;%
  add_osm_feature(key = &#39;landuse&#39;, value = &quot;forest&quot;) %&gt;%
  osmdata_sf () %&gt;%
  trim_osmdata (&quot;bb&quot;)
&#10;forest_points=forest$osm_points[1]</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '21, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/950b64fca0edc74f18b586c909247976?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael23&#39;s gravatar image" />
<p><span>Michael23</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael23 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Apr '21, 16:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span></p>
</div>
</div>
<div id="comments-container-79695" class="comments-container">
&#10;</div>
<div id="comment-tools-79695" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79695-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79699"></span>

<div id="answer-container-79699" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79699-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>I don't know any R programming, but the <code>bbox = "bb"</code> looks problematic. You need to specify coordinates. Or maybe it's a placeholder ?</p>
<p>If you try to load every <code>landuse=forest</code> in the world, it will fail without doubt.</p>
<p>Using overpass, you can load either really specific data (by name, or reference for exemple) worldwide, or specify a small bounding box. Exceeding one or the other limit will meet the timeout.</p>
<p>You should try your overpass requests with <a href="http://overpass-turbo.eu/">overpass-turbo</a> IMHO. You'll understand much more easily what is going on under the hood.</p>
<p>For example this <a href="http://overpass-turbo.eu/s/16h4">query</a> does what you're wishing, I think. I just used the convenient Assistant. Try to load it in your area of interest, to see if it works.</p>
<p>Also, you should be aware that <code>natural=wood</code> is nearly a synonym to <code>landuse=forest</code>, so you should probably load both, like in this <a href="http://overpass-turbo.eu/s/16h6">query</a>. See the <a href="https://wiki.openstreetmap.org/wiki/Forest">wiki</a> for more details.</p>
<p>If you want to make worldwide, or even countrywide, analysis, you'll have to download the raw osm data, and work locally.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '21, 16:33</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-79699" class="comments-container">
&#10;</div>
<div id="comment-tools-79699" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79699-form-container" class="comment-form-container">
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

