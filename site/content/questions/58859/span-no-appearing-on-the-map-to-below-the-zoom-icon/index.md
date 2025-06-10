+++
type = "question"
title = "Span no appearing on the map to below the zoom icon"
description = '''I have setup the following osm map with the below codes. I want the contents div to appear below the zoom icon but it doesnt seem to appear. Also when I run this function var setUpdateTimer = setInterval(function() { updateTimer(); },1000); the zoom icon disappear. I would to update the span box to ...'''
date = "2017-08-29T21:01:00Z"
lastmod = "2017-08-30T08:04:00Z"
weight = 58859
keywords = [ "leaflet", "refresh" ]
aliases = [ "/questions/58859" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Span no appearing on the map to below the zoom icon](/questions/58859/span-no-appearing-on-the-map-to-below-the-zoom-icon)

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
<span id="post-58859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58859-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have setup the following osm map with the below codes. I want the contents div to appear below the zoom icon but it doesnt seem to appear. Also when I run this function var setUpdateTimer = setInterval(function() { updateTimer(); },1000); the zoom icon disappear. I would to update the span box to show in how many seconds it will refresh the map. How make the span appear?</p>
<pre><code>function init() {
             map = L.map(&#39;map&#39;);
&#10;             L.tileLayer(&#39;http://{s}.tile.osm.org/{z}/{x}/{y}.png&#39;, {
                attribution: &#39;&amp;copy; &lt;a href=&quot;http://openstreetmap.org&quot;&gt;OpenStreetMap&lt;/a&gt; contributors&#39;,
                maxZoom: 18
             }).addTo(map);
&#10;             var test1 = new L.LatLng(-1.935114,30.082111); // geographical point (longitude and latitude)
             map.setView(test1, 13);
           var contents = document.createElement(&quot;div&quot;);
                             contents.style.width=&quot;300px&quot;;
                             contents.style.height=&quot;10px&quot;;
                             contents.style.top=&quot;100px&quot;;
                             //contents.style.margin=&quot;30px&quot;;
&#10;
                             contents.innerHTML=&quot;&lt;span style=&#39;z-index:5;position: absolute;padding: 12px 12px;background-color:white;border: 2px solid rgba(0,0,0,.15);border-radius: 2px;font-size: 14px;&#39; id=&#39;counter&#39; name=&#39;counter&#39;&gt;10 Seconds&lt;/span&gt;&quot;;
                             document.getElementById(&#39;map&#39;).appendChild(contents);
    }
&#10;
function updateTimer(){
            countUp++;
            countDown=refreshRate-countUp;
&#10;            var list = document.getElementById(&quot;map&quot;);
&#10;                            // If the &lt;ul&gt; element has any child nodes, remove its first child node
                            if (list.hasChildNodes()) {
                               var parent = document.getElementById(&quot;map&quot;);
                                    var child = parent.children[1];
                                    var childval = child.innerHTML;
                                    //document.getElementById(&quot;output&quot;).innerHTML=childval;
                                    //alert(&quot;childValue:&quot;+childval);
                                    parent.children[1].innerHTML=&quot;&lt;span style=&#39;z-index:5;position: absolute;padding: 12px 12px;background-color:white;border: 2px solid rgba(0,0,0,.15);border-radius: 2px;font-size: 14px;&#39; id=&#39;counter&#39; name=&#39;counter&#39;&gt;&quot;+countDown+&quot; Seconds&lt;/span&gt;&quot;;
                            }
            //alert(&quot;test : &quot;+document.getElementById(&quot;form2&quot;).elements[&quot;counter&quot;].innerHTML);
            if(refreshRate==countUp){
               //alert(&quot;TEST&quot;);
               var list = document.getElementById(&quot;map&quot;);
&#10;                            // If the &lt;ul&gt; element has any child nodes, remove its first child node
                            if (list.hasChildNodes()) {
                               var parent = document.getElementById(&quot;map&quot;);
                                    var child = parent.children[1];
                                    var childval = child.innerHTML;
                                    //document.getElementById(&quot;output&quot;).innerHTML=childval;
                                    //alert(&quot;childValue:&quot;+childval);
                                    parent.children[1].innerHTML=&quot;&lt;span style=&#39;z-index:5;position: absolute;padding: 12px 12px;background-color:white;border: 2px solid rgba(0,0,0,.15);border-radius: 2px;font-size: 14px;&#39; id=&#39;counter&#39; name=&#39;counter&#39;&gt;&quot;+refreshRate+&quot; Seconds&lt;/span&gt;&quot;;
                                countUp=0;
                                countDown=0;
                            }
&#10;            }
&#10;
        }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-refresh" rel="tag" title="see questions tagged &#39;refresh&#39;">refresh</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '17, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/26750873415fcbe30ebf2fdeab499d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newbie14&#39;s gravatar image" />
<p><span>newbie14</span><br />
<span class="score" title="31 reputation points">31</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newbie14 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Aug '17, 08:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-58859" class="comments-container">
<span id="58863"></span>
<div id="comment-58863" class="comment">
<div id="post-58863-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This question is better suited for <a href="http://stackoverflow.com/">http://stackoverflow.com/</a> since it is mainly about Leaflet and HTML but not about OSM.</p>
</div>
<div id="comment-58863-info" class="comment-info">
<span class="comment-age">(30 Aug '17, 08:04)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

