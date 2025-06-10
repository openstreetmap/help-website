+++
type = "question"
title = "storing the results of a  ruby-request @ overpass-api into a mysql-db"
description = '''helllo dear osm-experts new to Ruby - i need some advices - i plan to do some requests in osm-files. (openstreetmap) Question - how can i store the results on a Database - eg mysql or - (if you prefer postgresql) - note: my favorite db - at least at the moment is mysql here the code  require &#x27;open-u...'''
date = "2014-06-08T12:24:00Z"
lastmod = "2014-06-09T12:28:00Z"
weight = 33802
keywords = [ "database", "ruby", "linux" ]
aliases = [ "/questions/33802" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [storing the results of a ruby-request @ overpass-api into a mysql-db](/questions/33802/storing-the-results-of-a-ruby-request-overpass-api-into-a-mysql-db)

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
<span id="post-33802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33802-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>helllo dear osm-experts</p>
<p>new to Ruby - i need some advices -</p>
<p>i plan to do some requests in osm-files. (openstreetmap)</p>
<p>Question - how can i store the results on a Database - eg mysql or - (if you prefer postgresql) -</p>
<p>note: my favorite db - at least at the moment is mysql</p>
<p>here the code</p>
<blockquote>
<pre><code>require &#39;open-uri&#39;
require &quot;net/http&quot;
require &#39;rexml/document&#39;
&#10;def query_overpass(object_type, left,bottom,right,top, key, value)
   base_url = &quot;http://www.overpass-api.de/api/xapi?&quot;
   query_string = &quot;#{object_type}[bbox=#{left},#{bottom},#{right},#{top}][#{key}=#{value}]&quot;
   url = &quot;#{base_url}#{URI.encode(query_string)}&quot;
   resp = Net::HTTP.get_response(URI.parse(url))
   data = resp.body
   return data
end
&#10;overpass_result = REXML::Document.new(query_overpass(&quot;node&quot;,</code></pre>
<p>7.1,51.2,7.2,51.3,"amenity","restaurant|pub|ice_cream|food_court|fast_food|cafe|biergarten|bar|bakery|steak|pasta|pizza|sushi|asia|nightclub"))</p>
<pre><code>overpass_result.elements.each(&#39;osm/node&#39;)</code></pre>
<p>{|x| if !x.elements["tag[<span><span><span><span><span><span><span><span><span><span><span><span><span><span>@k</span></span></span></span></span></span></span></span></span></span></span></span></span></span>='name']"].nil? print x.elements["tag[<span><span><span><span><span><span><span><span><span><span><span><span><span><span>@k</span></span></span></span></span></span></span></span></span></span></span></span></span></span>='name']"].attributes["v"] end print " | "</p>
<pre><code>  if !x.elements[&quot;tag[@k=&#39;addr:postcode&#39;]&quot;].nil?
    print x.elements[&quot;tag[@k=&#39;addr:postcode&#39;]&quot;].attributes[&quot;v&quot;]
    print &quot;, &quot;
  end
  if !x.elements[&quot;tag[@k=&#39;addr:city&#39;]&quot;].nil?
    print x.elements[&quot;tag[@k=&#39;addr:city&#39;]&quot;].attributes[&quot;v&quot;]
    print &quot;, &quot;
  end
  if !x.elements[&quot;tag[@k=&#39;addr:street&#39;]&quot;].nil?
    print x.elements[&quot;tag[@k=&#39;addr:street&#39;]&quot;].attributes[&quot;v&quot;]
    print &quot;, &quot;
  end
  if !x.elements[&quot;tag[@k=&#39;addr:housenumber&#39;]&quot;].nil?
    print x.elements[&quot;tag[@k=&#39;addr:housenumber&#39;]&quot;].attributes[&quot;v&quot;]
  end
  print &quot; | &quot;
  print x.attributes[&quot;lat&quot;]
  print &quot; | &quot;
  print x.attributes[&quot;lon&quot;]
  print &quot; | &quot;
  if !x.elements[&quot;tag[@k=&#39;website&#39;]&quot;].nil?
    print x.elements[&quot;tag[@k=&#39;website&#39;]&quot;].attributes[&quot;v&quot;]
  end
  print &quot; | &quot;
  if !x.elements[&quot;tag[@k=&#39;amenity&#39;]&quot;].nil?
    print x.elements[&quot;tag[@k=&#39;amenity&#39;]&quot;].attributes[&quot;v&quot;]
    print &quot; | &quot;
  end
  puts
}</code></pre>
</blockquote>
<p>look forward to hear from you</p>
<p>again - i would love to store it on a mysql - database - if possible. If you would prefer postgresql - then i would takte this one.... ;-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span> <span class="post-tag tag-link-ruby" rel="tag" title="see questions tagged &#39;ruby&#39;">ruby</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '14, 12:24</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33802" class="comments-container">
&#10;</div>
<div id="comment-tools-33802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33802-form-container" class="comment-form-container">
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

<span id="33821"></span>

<div id="answer-container-33821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33821-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would suggest using postgresql with the PostGIS extension - it's much better at geographical support than MySQL.</p>
<p>For ruby I'd recommend the RGeo suite of tools - see <a href="https://github.com/rgeo/rgeo">https://github.com/rgeo/rgeo</a> . I use this for my projects, usually with the activerecord-postgis-adapter and rgeo-geojson gems too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jun '14, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-33821" class="comments-container">
&#10;</div>
<div id="comment-tools-33821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33821-form-container" class="comment-form-container">
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

