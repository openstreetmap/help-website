+++
type = "question"
title = "request from overpass-api endpoint"
description = '''Hi  what if i do not have the data on my machine - can i do a overpass-api request at the overpass-api endpoint: derived from here: http://forum.openstreetmap.org/viewtopic.php?pid=364460#p364460 _ and thanks go out to suncobald require &#x27;open-uri&#x27;   require &quot;net/http&quot;  require &#x27;rexml/document&#x27;   def...'''
date = "2014-06-12T13:56:00Z"
lastmod = "2014-06-12T20:03:00Z"
weight = 33918
keywords = [ "apache", "overpass", "linux", "mysql" ]
aliases = [ "/questions/33918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [request from overpass-api endpoint](/questions/33918/request-from-overpass-api-endpoint)

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
<span id="post-33918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33918-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-33918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>what if i do not have the data on my machine - can i do a overpass-api request at the overpass-api endpoint: derived from here: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=364460#p364460">http://forum.openstreetmap.org/viewtopic.php?pid=364460#p364460</a> _ and thanks go out to suncobald</p>
<pre><code>require &#39;open-uri&#39;
&#10;    require &quot;net/http&quot;
    require &#39;rexml/document&#39;
&#10;    def query_overpass(object_type, left,bottom,right,top, key, value)
       base_url = &quot;http://www.overpass-api.de/api/xapi?&quot;
       query_string = &quot;#{object_type}[bbox=#{left},#{bottom},#{right},#{top}][#{key}=#{value}]&quot;
       url = &quot;#{base_url}#{URI.encode(query_string)}&quot;
       resp = Net::HTTP.get_response(URI.parse(url))
       data = resp.body
       return data
    end
&#10;    overpass_result = REXML::Document.new(query_overpass(&quot;node&quot;, 7.1,51.2,7.2,51.3,&quot;amenity&quot;,&quot;restaurant|pub|ice_cream|food_court|fast_food|cafe|biergarten|bar|bakery|steak|pasta|pizza|sushi|asia|nightclub&quot;))
&#10;    overpass_result.elements.each(&#39;osm/node&#39;) {|x|
      if !x.elements[&quot;tag[@k=&#39;name&#39;]&quot;].nil?
        print x.elements[&quot;tag[@k=&#39;name&#39;]&quot;].attributes[&quot;v&quot;]
      end
      print &quot; | &quot;
&#10;      if !x.elements[&quot;tag[@k=&#39;addr:postcode&#39;]&quot;].nil?
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
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '14, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '14, 09:48</strong> </span></p>
</div>
</div>
<div id="comments-container-33918" class="comments-container">
<span id="33919"></span>
<div id="comment-33919" class="comment">
<div id="post-33919-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Sure, isn't that what your(?) code is already trying? It contacts <a href="http://www.overpass-api.de">http://www.overpass-api.de</a>. So what is your actual problem?</p>
</div>
<div id="comment-33919-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 14:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33925"></span>
<div id="comment-33925" class="comment">
<div id="post-33925-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh, well, SunCobalt created this script originally, here's the link to his forum post: <a href="http://forum.openstreetmap.org/viewtopic.php?pid=364460#p364460">http://forum.openstreetmap.org/viewtopic.php?pid=364460#p364460</a></p>
<p>Looks like the OP doesn't really know what to do with it?</p>
</div>
<div id="comment-33925-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 20:03)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-33918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33918-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

