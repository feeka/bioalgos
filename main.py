from flask import request, render_template, redirect, flash, url_for, Flask
from forms import *
from algorithms1 import *
from algorithms2 import *
from algorithms3 import *
from algorithms5 import *
app = Flask(__name__)

ALGORITHMS=[
    {
        'name':'Reverse Complement',
        'input': 'A DNA string Pattern',
        'output': 'Pattern, the reverse complement of Pattern.',
        'route': 'revcompl',
        'info':'http://rosalind.info/problems/ba1c/'
    },
    {
        'name': 'Pattern Matching',
        'input': 'Pattern and Genome',
        'output' : 'A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome',
        'route':'patmatch',
        'info':'http://rosalind.info/problems/ba1d/'
    }, 
    {
        'name':'Pattern Count',
        'input': 'Strings Text and Pattern',
        'output': ' Count(Text, Pattern)',
        'route':'patcount',
        'info':'http://rosalind.info/problems/ba1a/'
    },
    {
        'name': 'Frequent Words',
        'input': 'A string Text and an integer k',
        'output' : 'All most frequent k-mers in Text',
        'route' : 'freqwords',
        'info' : 'http://rosalind.info/problems/ba1b/'
    },
    {
        'name':'Frequent Words with Mismatches',
        'input': 'A string Text as well as integers k and d',
        'output': 'All most frequent k-mers with up to d mismatches in Text',
        'route':'freqwordsmism',
        'info':'http://rosalind.info/problems/ba1i/'
    },
    {
        'name': 'Hamming Distance',
        'input': 'Two DNA strings',
        'output' : 'An integer value representing the Hamming distance',
        'route' : 'hammingdist',
        'info' : 'http://rosalind.info/problems/ba1g/'
    },
    {
        'name': 'Minimum Skew',
        'input': 'A DNA string Genome',
        'output' : 'All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|)',
        'route' : 'minskew',
        'info' : 'http://rosalind.info/problems/ba1f/'
    },
    {
        'name': 'Motif Enumeration',
        'input': 'Integers k and d, followed by a collection of strings Dna',
        'output' : 'All (k, d)-motifs in Dna',
        'route' : 'motifenum',
        'info' : 'http://rosalind.info/problems/ba2a/'
    },
    {
        'name': 'Median String',
        'input': 'An integer k, followed by a collection of strings Dna',
        'output' : 'A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)',
        'route' : 'medianstring',
        'info' : 'http://rosalind.info/problems/ba2b/'
    },
    {
        'name': 'Genome Sequencing',
        'input': 'An integer k followed by a list of k-mers Patterns.',
        'output' : 'A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)',
        'route' : 'genseq',
        'info' : 'http://rosalind.info/problems/ba2b/'
    },
]

app.config['SECRET_KEY']="a286171ec581aac9872a89d13e6226a6"
@app.route('/')
def about():
    return render_template('about.html')

@app.route('/algorithms')
def hello_world():
    return render_template('index.html',algos=ALGORITHMS)


@app.route('/home/freqwords', methods=('GET', 'POST'))
def freqwords():
    form = FreqWordsForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        kval= int(form.k_val.data)
        result = FrequentWords(DNASeq,kval)
        return render_template('frequent_words.html',title="Frequent Words Algorithm", form=form, result=result)
    return render_template('frequent_words.html',title="Frequent Words Algorithm", form=form)

@app.route('/home/revcompl', methods=('GET', 'POST'))
def revcompl():
    form = ReverseComplementForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        result = ReverseComplement(DNASeq)
        return render_template('reverse_complement.html',title="Reverse Complement Algorithm", form=form, result=result)
    return render_template('reverse_complement.html',title="Reverse Complement Algorithm", form=form)

@app.route('/home/patmatch', methods=('GET', 'POST'))
def patmatch():
    form = PatternMatchingForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        pattern= form.pattern.data
        result = PatternMatching(pattern,DNASeq)
        return render_template('pattern_matching.html',title="Pattern Matching Problem", form=form, result=result)
    return render_template('pattern_matching.html',title="Pattern Matching Problem", form=form)

@app.route('/home/patcount', methods=('GET', 'POST'))
def patcount():
    form = PatternCountForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        pattern= form.pattern.data
        result = PatternCount(DNASeq,pattern)
        return render_template('pattern_count.html',title="Pattern Count", form=form, result=result)
    return render_template('pattern_count.html',title="Pattern Count", form=form)

@app.route('/home/hammingdist', methods=('GET', 'POST'))
def hammingdist():
    form = HammingDistanceForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        pattern_q = form.pattern_q.data
        pattern_p= form.pattern_p.data
        result = HammingDistance(pattern_q,pattern_p)
        return render_template('hamming_distance.html',title="Hamming Distance", form=form, result=result)
    return render_template('hamming_distance.html',title="Hamming Distance", form=form)

@app.route('/home/freqwordsmism', methods=('GET', 'POST'))
def freqwordsmism():
    form = FreqWordsWithMismatchForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        k_val= form.k_val.data
        distance=form.distance.data
        result = FrequentWordsWithMismatches(dna_seq,k_val,distance)
        print(result)
        return render_template('frequent_words_with_mismatches.html',title="Frequent words mismatches", form=form, result=result)
    return render_template('frequent_words_with_mismatches.html',title="Frequent words w/ mismatches", form=form)

@app.route('/home/minskew', methods=('GET', 'POST'))
def minskew():
    form = ReverseComplementForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        DNASeq = form.dna_seq.data
        result = MinimumSkew(DNASeq)
        return render_template('minimum_skew.html',title="Minimum Skew", form=form, result=result)
    return render_template('minimum_skew.html',title="Minimum Skew", form=form)


@app.route('/home/motifenum', methods=('GET', 'POST'))
def motifenum():
    form = FreqWordsWithMismatchForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        dna_update = dna_seq.split("\r\n")
        print(dna_update)
        k_val= form.k_val.data
        distance=form.distance.data
        result = motif_enumeration(dna_update,k_val,distance)
        print(result)
        return render_template('motif_enumeration.html',title="Motif Enumeration", form=form, result=result)
    return render_template('motif_enumeration.html',title="Motif Enumeration", form=form)

@app.route('/home/medianstring', methods=('GET', 'POST'))
def medianstring():
    form = FreqWordsForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        dna_update = dna_seq.split("\r\n")
        print(dna_update)
        k_val= int(form.k_val.data)
        result = MedianString(dna_update,k_val)
        print(result)
        return render_template('medianstring.html',title="Median String", form=form, result=result)
    return render_template('medianstring.html',title="Median String", form=form)

@app.route('/home/genseq', methods=('GET', 'POST'))
def genome_sequencing():
    form = ReverseComplementForm()
    if form.validate_on_submit():
        flash('Calculation successfully submitted','success')
        dna_seq = form.dna_seq.data
        dna_update = dna_seq.split("\r\n")
        print(dna_update)
        k_val= int(form.k_val.data)
        result = MedianString(dna_update,k_val)
        print(result)
        return render_template('medianstring.html',title="Median String", form=form, result=result)
    return render_template('medianstring.html',title="Median String", form=form)
# start listening
if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')
    
    