+++
type = "question"
title = "[Overpass-API] Difference between manual Overpass GeoJSON export (only LineString) and Overpass API result"
description = '''I would like to export the Nordlink power cable relation to GeoJSON. Until now I&#x27;m using the API with python-overpass and the following query: relation(5500685);(._;&amp;gt;;);out geom;  As output I&#x27;m getting the LineString two times (!) plus all points. Example: {  &quot;geometry&quot;: {  &quot;coordinates&quot;: [  6.59...'''
date = "2018-04-24T09:36:00Z"
lastmod = "2018-04-24T21:45:00Z"
weight = 63099
keywords = [ "overpassapi", "python", "geojson" ]
aliases = [ "/questions/63099" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Overpass-API\] Difference between manual Overpass GeoJSON export (only LineString) and Overpass API result](/questions/63099/overpass-api-difference-between-manual-overpass-geojson-export-only-linestring-and-overpass-api-result)

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
<span id="post-63099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63099-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to export the <a href="https://www.openstreetmap.org/relation/5500685">Nordlink power cable relation</a> to GeoJSON.</p>
<p>Until now I'm using the API with <a href="https://github.com/mvexel/overpass-api-python-wrapper">python-overpass</a> and the following query:</p>
<pre><code>relation(5500685);(._;&gt;;);out geom;</code></pre>
<p>As output I'm getting the LineString two times (!) plus all points. Example:</p>
<pre><code>{
  &quot;geometry&quot;: {
    &quot;coordinates&quot;: [
      6.5962545,
      58.181566
    ],
    &quot;type&quot;: &quot;Point&quot;
  },</code></pre>
<p>While when using the Overpass API manually (<a href="https://overpass-turbo.eu/s/yaT">Link</a>)</p>
<pre><code>[out:json][timeout:300];
(
relation(5500685);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>I only get the LineString:</p>
<pre><code>{
  &quot;type&quot;: &quot;FeatureCollection&quot;,
  &quot;features&quot;: [
    {
      &quot;type&quot;: &quot;Feature&quot;,
      &quot;properties&quot;: {
        &quot;@id&quot;: &quot;way/370147304&quot;,
        &quot;@relations&quot;: [
          {
            &quot;role&quot;: &quot;&quot;,
            &quot;rel&quot;: 5500685,
            &quot;reltags&quot;: {
              &quot;type&quot;: &quot;collection&quot;,
              &quot;wikidata&quot;: &quot;Q1961296&quot;,
              &quot;wikipedia&quot;: &quot;no:NordLink&quot;
            }
          }
        ]
      },
      &quot;geometry&quot;: {
        &quot;type&quot;: &quot;LineString&quot;,
        &quot;coordinates&quot;: [
          [
            6.6807119,
            58.2607599
          ],
          [
            6.694153,
            58.2131834
          ],
          [
            6.6534177,
            58.1893486
          ],
          [
            6.5962545,
            58.181566
          ],
          [
            6.4788896,
            58.1497393
          ],
          [
            6.4419395,
            58.0867718
          ],
          [
            8.4853879,
            54.2985972
          ],
          [
            8.7676507,
            54.179769
          ]
        ]
      },
      &quot;id&quot;: &quot;way/370147304&quot;
    }
  ]
}</code></pre>
<p>How can I get the same result (without points) like the manual query by using the API?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '18, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/bdb6a1b49c42d8be4b8d87f3096a3622?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Druzhba&#39;s gravatar image" />
<p><span>Druzhba</span><br />
<span class="score" title="150 reputation points">150</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Druzhba has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63099" class="comments-container">
<span id="63106"></span>
<div id="comment-63106" class="comment">
<div id="post-63106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The two queries you mention here are different, so it's logical that you'd get different results. Have you tried simply using the same query?</p>
</div>
<div id="comment-63106-info" class="comment-info">
<span class="comment-age">(24 Apr '18, 16:53)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="63108"></span>
<div id="comment-63108" class="comment">
<div id="post-63108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that Overpass-API doesn't output geojson, it outputs a json representation of the osm node/way/relation data model. Overpass Turbo has some code that converts the osm data model to geojson.</p>
</div>
<div id="comment-63108-info" class="comment-info">
<span class="comment-age">(24 Apr '18, 20:15)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="63114"></span>
<div id="comment-63114" class="comment">
<div id="post-63114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How to convert this json representation to plain geojson?</p>
</div>
<div id="comment-63114-info" class="comment-info">
<span class="comment-age">(24 Apr '18, 21:45)</span> <span class="comment-user userinfo">Druzhba</span>
</div>
</div>
</div>
<div id="comment-tools-63099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63099-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

