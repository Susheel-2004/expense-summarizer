from pymongo import MongoClient

def get_connection():
    connection_string = ""
    client = MongoClient(connection_string)

    db = client['G214']

    return db

"""
const transactionSchema = new Schema({
    user_id: {
        type:String,
        required: true
    },
    transaction_id : {
        type: String,
        default: uuidv4(),
        required: true,
    },
    type: {
        type: String,
        enum: ['Income', 'Expense'],
        required: true
    },
    amount: {
        type: Number,
        required: true,
        min: 0 // Prevent negative amounts
    },
    category_id: {
        type: String,
        required: false // Category can be null
    },
    description: {
        type: String,
        trim: true // Remove whitespace from both ends
    },
    transaction_date: {
        type: Date,
        default: Date.now
    }
}
"""

"""
const categorySchema = new Schema({ 
    category_id: {
        type: String,
        required: true,
        unique: true,
        trim: true
    },
    category_name: {
        type: String,
        required: true,
        trim: true
    },
    is_default: {
        type: Boolean,
        required: true
    }
})
"""
