+++
type = "question"
title = "Shadowbox.js opening but not display simple  content"
description = '''Ive created a world map using JVectorMap and am wanting to open a box using Shadowbox.js displaying various information about each highlighted country - In this example it&#x27;s specifically MENA countries. The map works and the pop-up works but my div TEST is not displaying at all, I am getting an erro...'''
date = "2022-11-10T07:23:00Z"
lastmod = "2022-11-10T14:36:00Z"
weight = 86130
keywords = [ "map", "api" ]
aliases = [ "/questions/86130" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Shadowbox.js opening but not display simple content](/questions/86130/shadowboxjs-opening-but-not-display-simple-content)

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
<span id="post-86130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86130-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ive created a world map using JVectorMap and am wanting to open a box using Shadowbox.js displaying various information about each highlighted country - In this example it's specifically MENA countries.</p>
<p>The map works and the pop-up works but my div</p>
<div>
TEST
</div>
is not displaying at all, I am getting an error: "It may have been moved, edited or deleted."
<p>Heres my code:</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;jVectorMap&lt;/title&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;IE=edge&quot;&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
  &lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;shadowbox.css&quot;&gt;
  &lt;link rel=&quot;stylesheet&quot; href=&quot;jquery-jvectormap-2.0.5.css&quot;&gt;
&#10;  &lt;script src=&quot;https://code.jquery.com/jquery-2.2.4.min.js&quot; integrity=&quot;sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=&quot; crossorigin=&quot;anonymous&quot;&gt;&lt;/script&gt;
&#10;  &lt;script src=&quot;jquery-jvectormap-2.0.5.min.js&quot;&gt;&lt;/script&gt;
  &lt;script src=&quot;jquery-jvectormap-world-mill-en.js&quot;&gt;&lt;/script&gt;
  &lt;script src=&quot;shadowbox.js&quot;&gt;&lt;/script&gt;
  &lt;script type=&quot;text/javascript&quot;&gt;
    Shadowbox.init({
    language: &#39;en&#39;,
    players: [&#39;iframe&#39;,&#39;html&#39;]
    });
    &lt;/script&gt; 
&lt;/head&gt;
&#10;&lt;body&gt;
  &lt;div id=&quot;world-map&quot; style=&quot;width: 600px; height: 400px&quot;&gt;&lt;/div&gt;
  &lt;script type=&quot;text/javascript&quot;&gt;
&#10;    $(function(){
&#10;      var codes = [&#39;DZ&#39;,&#39;EG&#39;,&#39;IR&#39;,&#39;IQ&#39;,&#39;IL&#39;,&#39;JO&#39;,&#39;KW&#39;,&#39;LB&#39;,&#39;LY&#39;,&#39;MA&#39;,&#39;OM&#39;,&#39;QA&#39;,&#39;SA&#39;,&#39;TN&#39;,&#39;AE&#39;,&#39;YE&#39;];
&#10;      $(&#39;#world-map&#39;).vectorMap({
        map: &#39;world_mill_en&#39;,
        zoomMax: 20,
        backgroundColor: &#39;#505050&#39;,
        regionStyle: {
          initial: {
            fill: &#39;#F6F5F4&#39;
          },
          hover: {
            fill: &#39;#F6F5F4&#39;,
            &quot;fill-opacity&quot;: 1
          },
          selected: {
            fill: &#39;#7B8B9B&#39;
          },
          selectedHover: {
            cursor: &#39;pointer&#39;,
            fill: &#39;#002142&#39;
          }
        },
        selectedRegions: [&#39;DZ&#39;,&#39;EG&#39;,&#39;IR&#39;,&#39;IQ&#39;,&#39;IL&#39;,&#39;JO&#39;,&#39;KW&#39;,&#39;LB&#39;,&#39;LY&#39;,&#39;MA&#39;,&#39;OM&#39;,&#39;QA&#39;,&#39;SA&#39;,&#39;TN&#39;,&#39;AE&#39;,&#39;YE&#39;], onRegionClick: function (event, code) {
          if($.inArray(code,codes) &gt; -1) {
            Shadowbox.open({
              content:    &#39;&lt;div&gt;TEST&lt;/div&gt;&#39;,
              title:      &quot;MENA&quot;,
              player:     &quot;iframe&quot;,
              height:     400,
              width:      640
            });
          }
        }
      });
    });
    &lt;/script&gt;
&#10;&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>Further down the line Id like to have a different message for each code but for now I'd just like to get this working.</p>
<p>Any help appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '22, 07:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a0aeddd76c4dd602f064ff9504e087ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="veerablog&#39;s gravatar image" />
<p><span>veerablog</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="veerablog has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86130" class="comments-container">
<span id="86131"></span>
<div id="comment-86131" class="comment">
<div id="post-86131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>How is this related to OpenStreetMap?</p>
</div>
<div id="comment-86131-info" class="comment-info">
<span class="comment-age">(10 Nov '22, 14:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86130" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86130-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

