+++
type = "question"
title = "Function to parse addr:flats tag to array in PostgreSQL?"
description = '''I have been using the addr:flats tag on apartment buildings which specifies a range of flat references, together with the building:flats tag which specifies the total number (quantity) of flats. The latter information is actually the bit I&#x27;m most interested in, as I am using the data (amongst other ...'''
date = "2018-10-14T10:37:00Z"
lastmod = "2018-10-15T15:52:00Z"
weight = 66340
keywords = [ "function", "addr_flats", "building_flats", "postgresql", "parsing" ]
aliases = [ "/questions/66340" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Function to parse addr:flats tag to array in PostgreSQL?](/questions/66340/function-to-parse-addrflats-tag-to-array-in-postgresql)

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
<span id="post-66340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66340-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been using the addr:flats tag on apartment buildings which specifies a range of flat references, together with the building:flats tag which specifies the total number (quantity) of flats. The latter information is actually the bit I'm most interested in, as I am using the data (amongst other purposes) to compute the number of leaflets required for delivery in a district (during political elections). I have two reservations though:</p>
<ol>
<li>The building:flats tag seems little used, for some reason</li>
<li>The value in it is technically redundant as it is computable from the addr:flats data.</li>
</ol>
<p>So I wondered if anyone has written or knows of a user-defined function I can use within PostgreSQL to parse an addr:flats tag into a comprehensive array of distinct values. As well as the addr:flats value, the function would need to be passed the addr:interpolation value (or null). The number of flats is then simply the length of the returned array. This would be functionally similar to parsing a page printing sequence - eg <a href="https://stackoverflow.com/questions/40161/does-c-sharp-have-built-in-support-for-parsing-page-number-strings">this</a> kind of thing - but I'm not much of a programmer and hoped I could steal someone else's work!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-addr_flats" rel="tag" title="see questions tagged &#39;addr_flats&#39;">addr_flats</span> <span class="post-tag tag-link-building_flats" rel="tag" title="see questions tagged &#39;building_flats&#39;">building_flats</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '18, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/99265127a23e440720864dbe51e0b48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Libarch&#39;s gravatar image" />
<p><span>Libarch</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Libarch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66340" class="comments-container">
&#10;</div>
<div id="comment-tools-66340" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66340-form-container" class="comment-form-container">
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

<span id="66349"></span>

<div id="answer-container-66349" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66349-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've had a go myself, and this is what I came up with. It seems to work OK on my test data, but any comments or improvements would be very welcome:</p>
<pre><code>CREATE OR REPLACE FUNCTION addr_flats_to_array(addr_flats text, addr_interpolation text DEFAULT NULL) RETURNS text[] AS $$
DECLARE
    part_range text[];
    part text;
    return_array text[];
    start_val int;
    end_val int;
    incr int;
BEGIN
    IF addr_flats IS NULL THEN
        RETURN NULL;
    ELSIF addr_flats ~ &#39;,&#39; THEN -- commas not permitted (other checks here?)
        RAISE NOTICE &#39;addr_flats_to_array: Illegal char in [%]&#39;, addr_flats;
        RETURN NULL;            
    END IF;
    FOREACH part IN ARRAY regexp_split_to_array(addr_flats, &#39;;&#39;)
    LOOP
        part_range := regexp_split_to_array(part, &#39;-&#39;);
        CASE array_length(part_range, 1)
            WHEN 1 THEN -- this case is treated as a single reference, not a range
                return_array := array_append(return_array, part);
                CONTINUE;
            WHEN 2 THEN -- this case is a range, ie two references separated by a hyphen
                IF part_range[1] ~ &#39;^\d+$&#39; AND part_range[2] ~ &#39;^\d+$&#39; THEN -- both values are integers
                    start_val := CAST(part_range[1] AS int);
                    end_val := CAST(part_range[2] AS int);
                    IF end_val &lt; start_val THEN
                        RAISE NOTICE &#39;addr_flats_to_array: Non-incremental range &quot;%&quot; in [%]&#39;, part, addr_flats;
                        RETURN NULL;
                    END IF;
                    CASE addr_interpolation
                        WHEN &#39;odd&#39; THEN
                            IF mod(start_val, 2) != 1 THEN
                                RAISE NOTICE &#39;addr_flats_to_array: Even start value &quot;%&quot; in odd-interpolated ranges [%]&#39;, start_val, addr_flats;
                                RETURN NULL;
                            END IF;
                            incr := 2;
                        WHEN &#39;even&#39; THEN
                            IF mod(start_val, 2) != 0 THEN
                                RAISE NOTICE &#39;addr_flats_to_array: Odd start value &quot;%&quot; in even-interpolated ranges [%]&#39;, start_val, addr_flats;
                                RETURN NULL;
                            END IF;
                            incr := 2;
                        ELSE
                            incr := 1;
                    END CASE;
                    FOR i IN start_val..end_val BY incr LOOP
                        return_array := array_append(return_array, CAST(i AS text));
                    END LOOP;
                ELSIF length(part_range[1]) = 1 AND length(part_range[2]) = 1 THEN -- both references are single non-integer chars
                    start_val := ascii(part_range[1]);
                    end_val := ascii(part_range[2]);
                    IF start_val &lt; ascii(&#39;A&#39;) OR end_val &gt; ascii(&#39;Z&#39;) OR end_val &lt; start_val THEN -- only capital letters can be used in a range
                        RAISE NOTICE &#39;addr_flats_to_array: Malformed alphabetic range &quot;%&quot; in [%]&#39;, part, addr_flats;
                        RETURN NULL;
                    END IF;
                    FOR i IN start_val..end_val LOOP
                        return_array := array_append(return_array, chr(i));
                    END LOOP;
                END IF;
            ELSE -- this shouldn&#39;t happen; eg &#39;1-3-9&#39; etc
                RAISE NOTICE &#39;addr_flats_to_array: Malformed range &quot;%&quot; in [%]&#39;, part, addr_flats;
                RETURN NULL;
        END CASE;
    END LOOP;
    RETURN return_array;
END;
$$ LANGUAGE plpgsql IMMUTABLE;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '18, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/99265127a23e440720864dbe51e0b48f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Libarch&#39;s gravatar image" />
<p><span>Libarch</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Libarch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66349" class="comments-container">
&#10;</div>
<div id="comment-tools-66349" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66349-form-container" class="comment-form-container">
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

