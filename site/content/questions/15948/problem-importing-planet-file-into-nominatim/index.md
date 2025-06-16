+++
type = "question"
title = "Problem importing Planet file into Nominatim"
description = '''After a gruesome night installing PostgreSQL 9.1, PostGIS 2 and Nominatim 2 on CentOS 6.3 using the instructions here, I am finally at the stage of importing a US planet file. Problem: In ~/Nominatim/utils, When I attempt to run ./setup.php --osm-file us-northeast.osm.pbf --all, the output I get end...'''
date = "2012-09-10T17:56:00Z"
lastmod = "2012-09-12T13:41:00Z"
weight = 15948
keywords = [ "openstreetmap", "postgresql", "nominatim", "osm", "postgis" ]
aliases = [ "/questions/15948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem importing Planet file into Nominatim](/questions/15948/problem-importing-planet-file-into-nominatim)

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
<span id="post-15948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>After a gruesome night installing PostgreSQL 9.1, PostGIS 2 and Nominatim 2 on CentOS 6.3 using the instructions <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">here</a>, I am finally at the stage of importing a US planet file.</p>
<p><strong>Problem:</strong> In <code>~/Nominatim/utils</code>, When I attempt to run <code>./setup.php --osm-file us-northeast.osm.pbf --all</code>, the output I get ends with:</p>
<pre><code> [&quot;type&quot;]=&gt;
      string(2) &quot;-&gt;&quot;
      [&quot;args&quot;]=&gt;
      array(2) {
        [0]=&gt;
        array(9) {
          [&quot;phptype&quot;]=&gt;
          string(5) &quot;pgsql&quot;
          [&quot;dbsyntax&quot;]=&gt;
          string(5) &quot;pgsql&quot;
          [&quot;username&quot;]=&gt;
          string(0) &quot;&quot;
          [&quot;password&quot;]=&gt;
          bool(false)
          [&quot;protocol&quot;]=&gt;
          string(3) &quot;tcp&quot;
          [&quot;hostspec&quot;]=&gt;
          string(0) &quot;&quot;
          [&quot;port&quot;]=&gt;
          bool(false)
          [&quot;socket&quot;]=&gt;
          bool(false)
          [&quot;database&quot;]=&gt;
          string(9) &quot;nominatim&quot;
        }
        [1]=&gt;
        bool(false)
      }
    }
    [5]=&gt;
    array(6) {
      [&quot;file&quot;]=&gt;
      string(35) &quot;/home/myusername/Nominatim/lib/db.php&quot;
      [&quot;line&quot;]=&gt;
      int(7)
      [&quot;function&quot;]=&gt;
      string(7) &quot;connect&quot;
      [&quot;class&quot;]=&gt;
      string(2) &quot;DB&quot;
      [&quot;type&quot;]=&gt;
      string(2) &quot;::&quot;
      [&quot;args&quot;]=&gt;
      array(2) {
        [0]=&gt;
        string(19) &quot;pgsql://@/nominatim&quot;
        [1]=&gt;
        bool(false)
      }
    }
    [6]=&gt;
    array(4) {
      [&quot;file&quot;]=&gt;
      string(40) &quot;/home/myusername/Nominatim/utils/setup.php&quot;
      [&quot;line&quot;]=&gt;
      int(118)
      [&quot;function&quot;]=&gt;
      string(5) &quot;getDB&quot;
      [&quot;args&quot;]=&gt;
      array(0) {
      }
    }
  }
  [&quot;callback&quot;]=&gt;
  NULL
}
DB Error: connect failed</code></pre>
<p>Any idea what went wrong? Do I need to create any database before doing this? Is it supposed to connect without a username and password as shown above?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Sep '12, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9a7101fe3ba50e621e91ee1edf9d27bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyxynyx&#39;s gravatar image" />
<p><span>nyxynyx</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyxynyx has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '12, 02:19</strong> </span></p>
</div>
</div>
<div id="comments-container-15948" class="comments-container">
<span id="15974"></span>
<div id="comment-15974" class="comment">
<div id="post-15974-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you cannot see a helpful answer here maybe your question is to specific for an FAQ.</p>
<p>In this case you can try again on one of the OSM mailing lists ( <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">https://wiki.openstreetmap.org/wiki/Mailing_lists</a> ) or the OSM forum.</p>
</div>
<div id="comment-15974-info" class="comment-info">
<span class="comment-age">(11 Sep '12, 16:52)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="16001"></span>
<div id="comment-16001" class="comment">
<div id="post-16001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have posted both to the geocoder mailing list and the OSM forum.</p>
</div>
<div id="comment-16001-info" class="comment-info">
<span class="comment-age">(12 Sep '12, 13:41)</span> <span class="comment-user userinfo">nyxynyx</span>
</div>
</div>
</div>
<div id="comment-tools-15948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15948-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

