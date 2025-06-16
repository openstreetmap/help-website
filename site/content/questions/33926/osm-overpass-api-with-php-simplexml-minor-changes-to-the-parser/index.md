+++
type = "question"
title = "OSM Overpass API with PHP SimpleXML :: minor changes to the parser"
description = '''new to the work with PHPSimpleXML so do not bear with me for askin newby questions. This is derived from here: http://stackoverflow.com/questions/16129184/osm-data-parsing-to-get-the-nodes-with-child I want to filter the data to get the nodes with special category. Here is sample of the OSM data I w...'''
date = "2014-06-12T20:15:00Z"
lastmod = "2014-06-12T20:15:00Z"
weight = 33926
keywords = [ "osm", "mysql", "export", "parsing" ]
aliases = [ "/questions/33926" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OSM Overpass API with PHP SimpleXML :: minor changes to the parser](/questions/33926/osm-overpass-api-with-php-simplexml-minor-changes-to-the-parser)

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
<span id="post-33926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33926-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-33926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>new to the work with PHPSimpleXML so do not bear with me for askin newby questions.</p>
<p>This is derived from here: <a href="http://stackoverflow.com/questions/16129184/osm-data-parsing-to-get-the-nodes-with-child">http://stackoverflow.com/questions/16129184/osm-data-parsing-to-get-the-nodes-with-child</a></p>
<p>I want to filter the data to get the nodes with special category. Here is sample of the OSM data I want to get the whole schools within an area. The first script runs well - but now i want to refine the search and add more tags. Finally i want to store all into the MySQL-db</p>
<p>So we need to make some XML parsing with PHP:</p>
<p>The following is a little OSM Overpass API example with PHP SimpleXML</p>
<pre><code>&lt;?php
/**
 * OSM Overpass API with PHP SimpleXML / XPath
 *
 * PHP Version: 5.4 - Can be back-ported to 5.3 by using 5.3 Array-Syntax (not PHP 5.4&#39;s square brackets)
 */
&#10;//
// 1.) Query an OSM Overpass API Endpoint
//
&#10;$query = &#39;node
  [&quot;amenity&quot;~&quot;.*&quot;]
  (38.415938460513274,16.06338500976562,39.52205163048525,17.51220703125);
out;&#39;;
&#10;$context = stream_context_create([&#39;http&#39; =&gt; [
    &#39;method&#39;  =&gt; &#39;POST&#39;,
    &#39;header&#39; =&gt; [&#39;Content-Type: application/x-www-form-urlencoded&#39;],
    &#39;content&#39; =&gt; &#39;data=&#39; . urlencode($query),
]]);
&#10;# please do not stress this service, this example is for demonstration purposes only.
$endpoint = &#39;http://overpass-api.de/api/interpreter&#39;;
libxml_set_streams_context($context);
$start = microtime(true);
&#10;$result = simplexml_load_file($endpoint);
printf(&quot;Query returned %2\$d node(s) and took %1\$.5f seconds.\n\n&quot;, microtime(true) - $start, count($result-&gt;node));
&#10;//
// 2.) Work with the XML Result
//
&#10;# get all school nodes with xpath
$xpath = &#39;//node[tag[@k = &quot;amenity&quot; and @v = &quot;school&quot;]]&#39;;
$schools = $result-&gt;xpath($xpath);
printf(&quot;%d School(s) found:\n&quot;, count($schools));
foreach ($schools as $index =&gt; $school)
{
    # Get the name of the school (if any), again with xpath
    list($name) = $school-&gt;xpath(&#39;tag[@k = &quot;name&quot;]/@v&#39;) + [&#39;(unnamed)&#39;];
    printf(&quot;#%02d: ID:%&#39; -10s  [%s,%s]  %s\n&quot;, $index, $school[&#39;id&#39;], $school[&#39;lat&#39;], $school[&#39;lon&#39;], $name);
}
&#10;?&gt;</code></pre>
<p>The second part is more interesting. That is querying the XML data you have already. This is most easily done with xpath, the used PHP XML library is based on libxml which supports XPath 1.0 which covers the various querying needs very well. The following example lists all schools and tries to obtain their names as well. I have not covered translations yet because my sample data didn't have those, but you can also look for all kind of names including translations and just prefer a specific one):</p>
<p>The key point here are the xpath queries. Two are used, the first one to get the nodes that have certain tags. I think this is the most interesting one for you:</p>
<pre><code>//node[tag[@k = &quot;amenity&quot; and @v = &quot;school&quot;]]</code></pre>
<p>This line says: Give me all node elements that have a tag element inside which has the k attribute value "amenity" and the v attribute value "school". This is the condition you have to filter out those nodes that are tagged with amenity school. Further on xpath is used again, now relative to those school nodes to see if there is a name and if so to fetch it:</p>
<pre><code>tag[@k = &quot;name&quot;]/@v&#39;</code></pre>
<p>This line says: Relative to the current node, give me the v attribute from a tag element that as the k attribute value "name". As you can see, some parts are again similar to the line before. I think you can both adopt them to your needs. Because not all school nodes have a name, a default string is provided for display purposes by adding it to the (then empty) result array:</p>
<pre><code>list($name) = $school-&gt;xpath(&#39;tag[@k = &quot;name&quot;]/@v&#39;) + [&#39;(unnamed)&#39;];
                                                    ^^^^^^^^^^^^^^^
                                                Provide Default Value</code></pre>
<p>so far so good: <strong>note</strong>. i need to have the adress-data, of the school with</p>
<p>cf <a href="https://wiki.openstreetmap.org/wiki/Key:addr">https://wiki.openstreetmap.org/wiki/Key:addr</a></p>
<p>and even more important</p>
<p>cf <a href="https://wiki.openstreetmap.org/wiki/Key:contact">https://wiki.openstreetmap.org/wiki/Key:contact</a></p>
<pre><code>contact:phone 
contact:fax     
contact:website 
contact:email</code></pre>
<p>btw. here my results for that code-example:</p>
<pre><code>martin@linux-70ce:~/php&gt; 
martin@linux-70ce:~/php&gt; php osm1.php
Query returned 1691 node(s) and took 3.34569 seconds.
&#10;23 School(s) found:
#00: ID:332534486   [39.5017565,16.2721899]  Scuola Primaria
#01: ID:1428094278  [39.3320912,16.1862820]  (unnamed)
#02: ID:1822746784  [38.9075566,16.5776597]  (unnamed)
#03: ID:1822755951  [38.9120272,16.5713431]  (unnamed)
#04: ID:1903859699  [38.6830409,16.5522243]  Liceo Scientifico Statale A. Guarasci
#05: ID:2002566438  [39.1349460,16.0736446]  (unnamed)
#06: ID:2056891127  [39.4106679,16.8254844]  (unnamed)
#07: ID:2056892999  [39.4124687,16.8286119]  (unnamed)
#08: ID:2272010226  [39.4481717,16.2894353]  SCUOLA DELL&#39;INFANZIA SAN FRANCESCO
#09: ID:2272017152  [39.4502366,16.2807664]  Scuola Media
#10: ID:2358307794  [39.5015031,16.3905965]  I.I.S.S. Liceo Statale V. Iulia
#11: ID:2358307796  [39.4926280,16.3853662]  Liceo Classico
#12: ID:2358307797  [39.4973761,16.3858275]  Scuola Media
#13: ID:2358307800  [39.5015527,16.3941156]  I.T.C. e per Geometri
#14: ID:2358307801  [39.4983862,16.3807796]  Istituto Professionale
#15: ID:2358344885  [39.4854617,16.3832419]  Istituto Tecnico Statale Commerciale G. Falcone
martin@linux-70ce:~/php&gt;</code></pre>
<p>note. i need to have the adress-data, of the shool with</p>
<p>and even more important <a href="https://wiki.openstreetmap.org/wiki/Key:contact">https://wiki.openstreetmap.org/wiki/Key:contact</a></p>
<pre><code>contact:phone 
contact:fax     
contact:website 
contact:email</code></pre>
<p>How to add this .. into the query? and how to finally store all into the MySQL-db?</p>
<p><strong>update</strong>: can i rework like so:</p>
<pre><code>$xml = file_get_contents($url);
$data = new SimpleXMLElement($xml);
&#10;$data variable contains the following:
&#10;SimpleXMLElement Object
(
    [@attributes] =&gt; Array
        (
            [timestamp] =&gt; Sat, 15 Jun 13 20:02:13 +0000
            [attribution] =&gt; Data ÂŠ OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright
            [querystring] =&gt; Bucharest-Romania
            [polygon] =&gt; false
            [exclude_place_ids] =&gt; 331526
            [more_url] =&gt; http://nominatim.openstreetmap.org/search?format=xml&amp;exclude_place_ids=331526&amp;q=Bucharest-Romania
        )
&#10;    [place] =&gt; SimpleXMLElement Object
        (
            [@attributes] =&gt; Array
                (
                    [place_id] =&gt; 331526
                    [osm_type] =&gt; node
                    [osm_id] =&gt; 96209423
                    [place_rank] =&gt; 15
                    [boundingbox] =&gt; 44.4361381530762,44.4361419677734,26.1027431488037,26.1027450561523
                    [lat] =&gt; 44.436139
                    [lon] =&gt; 26.1027436
                    [display_name] =&gt; BucureČti, Sector 2, Bucuresti, RomĂ˘nia, European Union
                    [class] =&gt; place
                    [type] =&gt; city
                    [importance] =&gt; 0.73231672860554
                    [icon] =&gt; http://nominatim.openstreetmap.org/images/mapicons/poi_place_city.p.20.png
                )
&#10;        )
&#10;)</code></pre>
<p>look forward to hear from you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '14, 20:15</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '14, 09:43</strong> </span></p>
</div>
</div>
<div id="comments-container-33926" class="comments-container">
&#10;</div>
<div id="comment-tools-33926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33926-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

