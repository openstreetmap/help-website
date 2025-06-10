+++
type = "question"
title = "Extension not found"
description = '''I enter de command: ./utils/setup.php --osm-file ~/brazil-latest.osm --all 2&amp;gt;&amp;amp;1 | tee setup.log  And returns error: ERROR: DB Error: extension not found Complete error message: Create DB Setup DB string(19) &quot;pgsql://@/nominatim&quot; object(DB_Error)#4 (8) {  [&quot;error_message_prefix&quot;]=&amp;gt;  string(...'''
date = "2015-11-12T18:17:00Z"
lastmod = "2017-09-27T20:49:00Z"
weight = 46549
keywords = [ "nominatim", "installation" ]
aliases = [ "/questions/46549" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extension not found](/questions/46549/extension-not-found)

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
<span id="post-46549-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46549-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-46549-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I enter de command:</p>
<pre><code>./utils/setup.php --osm-file ~/brazil-latest.osm  --all  2&gt;&amp;1 | tee setup.log</code></pre>
<p>And returns error: <strong>ERROR: DB Error: extension not found</strong></p>
<p>Complete error message:</p>
<pre><code>Create DB
Setup DB
string(19) &quot;pgsql://@/nominatim&quot;
object(DB_Error)#4 (8) {
  [&quot;error_message_prefix&quot;]=&gt;
  string(0) &quot;&quot;
  [&quot;mode&quot;]=&gt;
  int(1)
  [&quot;level&quot;]=&gt;
  int(1024)
  [&quot;code&quot;]=&gt;
  int(-25)
  [&quot;message&quot;]=&gt;
  string(29) &quot;DB Error: extension not found&quot;
  [&quot;userinfo&quot;]=&gt;
  string(55) &quot; [DB Error: extension not found] ** pgsql://@/nominatim&quot;
  [&quot;backtrace&quot;]=&gt;
  array(7) {
    [0]=&gt;
    array(6) {
      [&quot;file&quot;]=&gt;
      string(21) &quot;/usr/share/php/DB.php&quot;
      [&quot;line&quot;]=&gt;
      int(967)
      [&quot;function&quot;]=&gt;
      string(10) &quot;PEAR_Error&quot;
      [&quot;class&quot;]=&gt;
      string(10) &quot;PEAR_Error&quot;
      [&quot;type&quot;]=&gt;
      string(2) &quot;-&gt;&quot;
      [&quot;args&quot;]=&gt;
      array(5) {
        [0]=&gt;
        string(29) &quot;DB Error: extension not found&quot;
        [1]=&gt;
        int(-25)
        [2]=&gt;
        int(1)
        [3]=&gt;
        int(1024)
        [4]=&gt;
        string(32) &quot; [DB Error: extension not found]&quot;
      }
    }
    [1]=&gt;
    array(7) {
      [&quot;file&quot;]=&gt;
      string(23) &quot;/usr/share/php/PEAR.php&quot;
      [&quot;line&quot;]=&gt;
      int(531)
      [&quot;function&quot;]=&gt;
      string(8) &quot;DB_Error&quot;
      [&quot;class&quot;]=&gt;
      string(8) &quot;DB_Error&quot;
      [&quot;object&quot;]=&gt;
      *RECURSION*
      [&quot;type&quot;]=&gt;
      string(2) &quot;-&gt;&quot;
      [&quot;args&quot;]=&gt;
      array(4) {
        [0]=&gt;
        int(-25)
        [1]=&gt;
        int(1)
        [2]=&gt;
        int(1024)
        [3]=&gt;
        string(32) &quot; [DB Error: extension not found]&quot;
      }
    }
    [2]=&gt;
    array(7) {
      [&quot;file&quot;]=&gt;
      string(28) &quot;/usr/share/php/DB/common.php&quot;
      [&quot;line&quot;]=&gt;
      int(1907)
      [&quot;function&quot;]=&gt;
      string(10) &quot;raiseError&quot;
      [&quot;class&quot;]=&gt;
      string(4) &quot;PEAR&quot;
      [&quot;object&quot;]=&gt;
      object(DB_pgsql)#3 (28) {
        [&quot;phptype&quot;]=&gt;
        string(5) &quot;pgsql&quot;
        [&quot;dbsyntax&quot;]=&gt;
        string(5) &quot;pgsql&quot;
        [&quot;features&quot;]=&gt;
        array(7) {
          [&quot;limit&quot;]=&gt;
          string(5) &quot;alter&quot;
          [&quot;new_link&quot;]=&gt;
          string(5) &quot;4.3.0&quot;
          [&quot;numrows&quot;]=&gt;
          bool(true)
          [&quot;pconnect&quot;]=&gt;
          bool(true)
          [&quot;prepare&quot;]=&gt;
          bool(false)
          [&quot;ssl&quot;]=&gt;
          bool(true)
          [&quot;transactions&quot;]=&gt;
          bool(true)
        }
        [&quot;errorcode_map&quot;]=&gt;
        array(0) {
        }
        [&quot;connection&quot;]=&gt;
        NULL
        [&quot;dsn&quot;]=&gt;
        array(0) {
        }
        [&quot;autocommit&quot;]=&gt;
        bool(true)
        [&quot;transaction_opcount&quot;]=&gt;
        int(0)
        [&quot;affected&quot;]=&gt;
        int(0)
        [&quot;row&quot;]=&gt;
        array(0) {
        }
        [&quot;_num_rows&quot;]=&gt;
        array(0) {
        }
        [&quot;fetchmode&quot;]=&gt;
        int(1)
        [&quot;fetchmode_object_class&quot;]=&gt;
        string(8) &quot;stdClass&quot;
        [&quot;was_connected&quot;]=&gt;
        NULL
        [&quot;last_query&quot;]=&gt;
        string(0) &quot;&quot;
        [&quot;options&quot;]=&gt;
        array(8) {
          [&quot;result_buffering&quot;]=&gt;
          int(500)
          [&quot;persistent&quot;]=&gt;
          bool(false)
          [&quot;ssl&quot;]=&gt;
          bool(false)
          [&quot;debug&quot;]=&gt;
          int(0)
          [&quot;seqname_format&quot;]=&gt;
          string(6) &quot;%s_seq&quot;
          [&quot;autofree&quot;]=&gt;
          bool(false)
          [&quot;portability&quot;]=&gt;
          int(0)
          [&quot;optimize&quot;]=&gt;
          string(11) &quot;performance&quot;
        }
        [&quot;last_parameters&quot;]=&gt;
        array(0) {
        }
        [&quot;prepare_tokens&quot;]=&gt;
        array(0) {
        }
        [&quot;prepare_types&quot;]=&gt;
        array(0) {
        }
        [&quot;prepared_queries&quot;]=&gt;
        array(0) {
        }
        [&quot;_last_query_manip&quot;]=&gt;
        bool(false)
        [&quot;_next_query_manip&quot;]=&gt;
        bool(false)
        [&quot;_debug&quot;]=&gt;
        bool(false)
        [&quot;_default_error_mode&quot;]=&gt;
        NULL
        [&quot;_default_error_options&quot;]=&gt;
        NULL
        [&quot;_default_error_handler&quot;]=&gt;
        string(0) &quot;&quot;
        [&quot;_error_class&quot;]=&gt;
        string(8) &quot;DB_Error&quot;
        [&quot;_expected_errors&quot;]=&gt;
        array(0) {
        }
      }
      [&quot;type&quot;]=&gt;
      string(2) &quot;-&gt;&quot;
      [&quot;args&quot;]=&gt;
      array(7) {
        [0]=&gt;
        NULL
        [1]=&gt;
        int(-25)
        [2]=&gt;
        NULL
        [3]=&gt;
        NULL
        [4]=&gt;
        string(32) &quot; [DB Error: extension not found]&quot;
        [5]=&gt;
        string(8) &quot;DB_Error&quot;
        [6]=&gt;
        bool(true)
      }
    }
    [3]=&gt;
    array(7) {
      [&quot;file&quot;]=&gt;
      string(27) &quot;/usr/share/php/DB/pgsql.php&quot;
      [&quot;line&quot;]=&gt;
      int(212)
      [&quot;function&quot;]=&gt;
      string(10) &quot;raiseError&quot;
      [&quot;class&quot;]=&gt;
      string(9) &quot;DB_common&quot;
      [&quot;object&quot;]=&gt;
      object(DB_pgsql)#3 (28) {
        [&quot;phptype&quot;]=&gt;
        string(5) &quot;pgsql&quot;
        [&quot;dbsyntax&quot;]=&gt;
        string(5) &quot;pgsql&quot;
        [&quot;features&quot;]=&gt;
        array(7) {
          [&quot;limit&quot;]=&gt;
          string(5) &quot;alter&quot;
          [&quot;new_link&quot;]=&gt;
          string(5) &quot;4.3.0&quot;
          [&quot;numrows&quot;]=&gt;
          bool(true)
          [&quot;pconnect&quot;]=&gt;
          bool(true)
          [&quot;prepare&quot;]=&gt;
          bool(false)
          [&quot;ssl&quot;]=&gt;
          bool(true)
          [&quot;transactions&quot;]=&gt;
          bool(true)
        }
        [&quot;errorcode_map&quot;]=&gt;
        array(0) {
        }
        [&quot;connection&quot;]=&gt;
        NULL
        [&quot;dsn&quot;]=&gt;
        array(0) {
        }
        [&quot;autocommit&quot;]=&gt;
        bool(true)
        [&quot;transaction_opcount&quot;]=&gt;
        int(0)
        [&quot;affected&quot;]=&gt;
        int(0)
        [&quot;row&quot;]=&gt;
        array(0) {
        }
        [&quot;_num_rows&quot;]=&gt;
        array(0) {
        }
        [&quot;fetchmode&quot;]=&gt;
        int(1)
        [&quot;fetchmode_object_class&quot;]=&gt;
        string(8) &quot;stdClass&quot;
        [&quot;was_connected&quot;]=&gt;
        NULL
        [&quot;last_query&quot;]=&gt;
        string(0) &quot;&quot;
        [&quot;options&quot;]=&gt;
        array(8) {
          [&quot;result_buffering&quot;]=&gt;
          int(500)
          [&quot;persistent&quot;]=&gt;
          bool(false)
          [&quot;ssl&quot;]=&gt;
          bool(false)
          [&quot;debug&quot;]=&gt;
          int(0)
          [&quot;seqname_format&quot;]=&gt;
          string(6) &quot;%s_seq&quot;
          [&quot;autofree&quot;]=&gt;
          bool(false)
          [&quot;portability&quot;]=&gt;
          int(0)
          [&quot;optimize&quot;]=&gt;
          string(11) &quot;performance&quot;
        }
        [&quot;last_parameters&quot;]=&gt;
        array(0) {
        }
        [&quot;prepare_tokens&quot;]=&gt;
        array(0) {
        }
        [&quot;prepare_types&quot;]=&gt;
        array(0) {
        }
        [&quot;prepared_queries&quot;]=&gt;
        array(0) {
        }
        [&quot;_last_query_manip&quot;]=&gt;
        bool(false)
        [&quot;_next_query_manip&quot;]=&gt;
        bool(false)
        [&quot;_debug&quot;]=&gt;
        bool(false)
        [&quot;_default_error_mode&quot;]=&gt;
        NULL
        [&quot;_default_error_options&quot;]=&gt;
        NULL
        [&quot;_default_error_handler&quot;]=&gt;
        string(0) &quot;&quot;
        [&quot;_error_class&quot;]=&gt;
        string(8) &quot;DB_Error&quot;
        [&quot;_expected_errors&quot;]=&gt;
        array(0) {
        }
      }
      [&quot;type&quot;]=&gt;
      string(2) &quot;-&gt;&quot;
      [&quot;args&quot;]=&gt;
      array(1) {
        [0]=&gt;
        int(-25)
      }
    }
    [4]=&gt;
    array(7) {
      [&quot;file&quot;]=&gt;
      string(21) &quot;/usr/share/php/DB.php&quot;
      [&quot;line&quot;]=&gt;
      int(557)
      [&quot;function&quot;]=&gt;
      string(7) &quot;connect&quot;
      [&quot;class&quot;]=&gt;
      string(8) &quot;DB_pgsql&quot;
      [&quot;object&quot;]=&gt;
      object(DB_pgsql)#3 (28) {
        [&quot;phptype&quot;]=&gt;
        string(5) &quot;pgsql&quot;
        [&quot;dbsyntax&quot;]=&gt;
        string(5) &quot;pgsql&quot;
        [&quot;features&quot;]=&gt;
        array(7) {
          [&quot;limit&quot;]=&gt;
          string(5) &quot;alter&quot;
          [&quot;new_link&quot;]=&gt;
          string(5) &quot;4.3.0&quot;
          [&quot;numrows&quot;]=&gt;
          bool(true)
          [&quot;pconnect&quot;]=&gt;
          bool(true)
          [&quot;prepare&quot;]=&gt;
          bool(false)
          [&quot;ssl&quot;]=&gt;
          bool(true)
          [&quot;transactions&quot;]=&gt;
          bool(true)
        }
        [&quot;errorcode_map&quot;]=&gt;
        array(0) {
        }
        [&quot;connection&quot;]=&gt;
        NULL
        [&quot;dsn&quot;]=&gt;
        array(0) {
        }
        [&quot;autocommit&quot;]=&gt;
        bool(true)
        [&quot;transaction_opcount&quot;]=&gt;
        int(0)
        [&quot;affected&quot;]=&gt;
        int(0)
        [&quot;row&quot;]=&gt;
        array(0) {
        }
        [&quot;_num_rows&quot;]=&gt;
        array(0) {
        }
        [&quot;fetchmode&quot;]=&gt;
        int(1)
        [&quot;fetchmode_object_class&quot;]=&gt;
        string(8) &quot;stdClass&quot;
        [&quot;was_connected&quot;]=&gt;
        NULL
        [&quot;last_query&quot;]=&gt;
        string(0) &quot;&quot;
        [&quot;options&quot;]=&gt;
        array(8) {
          [&quot;result_buffering&quot;]=&gt;
          int(500)
          [&quot;persistent&quot;]=&gt;
          bool(false)
          [&quot;ssl&quot;]=&gt;
          bool(false)
          [&quot;debug&quot;]=&gt;
          int(0)
          [&quot;seqname_format&quot;]=&gt;
          string(6) &quot;%s_seq&quot;
          [&quot;autofree&quot;]=&gt;
          bool(false)
          [&quot;portability&quot;]=&gt;
          int(0)
          [&quot;optimize&quot;]=&gt;
          string(11) &quot;performance&quot;
        }
        [&quot;last_parameters&quot;]=&gt;
        array(0) {
        }
        [&quot;prepare_tokens&quot;]=&gt;
        array(0) {
        }
        [&quot;prepare_types&quot;]=&gt;
        array(0) {
        }
        [&quot;prepared_queries&quot;]=&gt;
        array(0) {
        }
        [&quot;_last_query_manip&quot;]=&gt;
        bool(false)
        [&quot;_next_query_manip&quot;]=&gt;
        bool(false)
        [&quot;_debug&quot;]=&gt;
        bool(false)
        [&quot;_default_error_mode&quot;]=&gt;
        NULL
        [&quot;_default_error_options&quot;]=&gt;
        NULL
        [&quot;_default_error_handler&quot;]=&gt;
        string(0) &quot;&quot;
        [&quot;_error_class&quot;]=&gt;
        string(8) &quot;DB_Error&quot;
        [&quot;_expected_errors&quot;]=&gt;
        array(0) {
        }
      }
      [&quot;type&quot;]=&gt;
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
      string(39) &quot;/home/ubuntu/Nominatim-2.4.0/lib/db.php&quot;
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
      string(44) &quot;/home/ubuntu/Nominatim-2.4.0/utils/setup.php&quot;
      [&quot;line&quot;]=&gt;
      int(112)
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
ERROR: DB Error: extension not found
DB Error: extension not found</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '15, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/90d0aa1917d54b295653368c358c0359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeancz&#39;s gravatar image" />
<p><span>jeancz</span><br />
<span class="score" title="47 reputation points">47</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeancz has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '15, 21:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46549" class="comments-container">
<span id="46551"></span>
<div id="comment-46551" class="comment">
<div id="post-46551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is a little too concise. I would check that your PostgreSQL database has at least PostGIS, and hstore installed. We really need to see more of the error message to provide further guidance.</p>
</div>
<div id="comment-46551-info" class="comment-info">
<span class="comment-age">(12 Nov '15, 19:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46549" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46549-form-container" class="comment-form-container">
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

<span id="46567"></span>

<div id="answer-container-46567" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>SOLVED.</p>
<p>I created a new virtual machine and reinstall all.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/90d0aa1917d54b295653368c358c0359?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeancz&#39;s gravatar image" />
<p><span>jeancz</span><br />
<span class="score" title="47 reputation points">47</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeancz has one accepted answer">33%</span></p>
</div>
</div>
<div id="comments-container-46567" class="comments-container">
&#10;</div>
<div id="comment-tools-46567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46567-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59862"></span>

<div id="answer-container-59862" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59862-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>this worked for me:</p>
<blockquote>
<p>dpkg --get-selections | grep -i php</p>
</blockquote>
<p>...</p>
<p>php5.6-pgsql install</p>
<p>php7.0-pgsql deinstall &lt;--- look</p>
<p>...</p>
<blockquote>
<p>sudo apt-get install php7.0-pgsql</p>
</blockquote>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '17, 20:49</strong></p>
<img src="https://secure.gravatar.com/avatar/46f203350f96ab645a0a04ed99cfa0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Carlos%20Brys&#39;s gravatar image" />
<p><span>Carlos Brys</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Carlos Brys has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Sep '17, 20:51</strong> </span></p>
</div>
</div>
<div id="comments-container-59862" class="comments-container">
&#10;</div>
<div id="comment-tools-59862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59862-form-container" class="comment-form-container">
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

